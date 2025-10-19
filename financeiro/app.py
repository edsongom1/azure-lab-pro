import streamlit as st
from PyPDF2 import PdfReader
from openai import OpenAI
from typing import List
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

# ==============================
# 🧭 Configuração da Página
# ==============================
st.set_page_config(
    page_title="Busca Inteligente em PDFs - Mercado Financeiro",
    page_icon="📊",
    layout="wide"
)

# ==============================
# 🧠 Cabeçalho
# ==============================
st.title("📊 Sistema de Busca Inteligente para PDFs")
st.markdown("### Análise de documentos sobre Mercado Financeiro com IA (GPT-4)")

# ==============================
# ⚙️ Sidebar
# ==============================
with st.sidebar:
    st.header("⚙️ Configurações")
    
    api_key = st.text_input("🔑 OpenAI API Key", type="password", help="Insira sua chave da OpenAI")

    st.markdown("---")
    st.header("📁 Upload de PDFs")
    uploaded_files = st.file_uploader(
        "Carregue seus arquivos PDF",
        type=['pdf'],
        accept_multiple_files=True
    )

    st.markdown("---")
    st.markdown("""
    ### 💡 Exemplos de perguntas:
    - Qual foi o impacto da taxa Selic?
    - Como funciona a alocação de ativos?
    - Quais são as tendências do mercado?
    """)

# ==============================
# 📄 Funções auxiliares
# ==============================

def extract_text_from_pdfs(pdf_files):
    """Extrai texto de múltiplos PDFs."""
    text = ""
    for pdf_file in pdf_files:
        try:
            pdf_reader = PdfReader(pdf_file)
            for page in pdf_reader.pages:
                page_text = page.extract_text()
                if page_text:
                    text += page_text + "\n"
        except Exception as e:
            st.error(f"Erro ao ler {pdf_file.name}: {str(e)}")
    return text


def split_text_into_chunks(text: str, chunk_size: int = 1000, overlap: int = 200) -> List[str]:
    """Divide o texto em chunks menores."""
    chunks = []
    start = 0
    text_length = len(text)
    
    while start < text_length:
        end = start + chunk_size
        chunk = text[start:end]
        chunks.append(chunk)
        start += chunk_size - overlap
    
    return chunks


def get_embedding(text: str, client) -> List[float]:
    """Obtém embedding usando OpenAI."""
    try:
        response = client.embeddings.create(
            input=text,
            model="text-embedding-3-small"
        )
        return response.data[0].embedding
    except Exception as e:
        st.error(f"Erro ao gerar embedding: {str(e)}")
        return []


def find_relevant_chunks(query: str, chunks: List[str], embeddings: List, client, top_k: int = 3) -> List[str]:
    """Encontra os chunks mais relevantes para a pergunta."""
    query_embedding = get_embedding(query, client)
    
    if not query_embedding:
        return chunks[:top_k]
    
    # Calcular similaridade
    similarities = cosine_similarity([query_embedding], embeddings)[0]
    
    # Pegar os top_k mais similares
    top_indices = np.argsort(similarities)[-top_k:][::-1]
    
    return [chunks[i] for i in top_indices]


def generate_answer(question: str, context: str, chat_history: List, client) -> str:
    """Gera resposta usando GPT-4."""
    
    # Construir histórico de mensagens
    messages = [
        {"role": "system", "content": "Você é um assistente especializado em mercado financeiro. Responda baseado apenas no contexto fornecido. Se a informação não estiver no contexto, diga que não encontrou."}
    ]
    
    # Adicionar histórico
    for msg in chat_history[-6:]:  # Últimas 3 interações
        messages.append({"role": msg["role"], "content": msg["content"]})
    
    # Adicionar pergunta atual com contexto
    messages.append({
        "role": "user",
        "content": f"Contexto dos documentos:\n{context}\n\nPergunta: {question}"
    })
    
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=messages,
            temperature=0.7,
            max_tokens=1000
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Erro ao gerar resposta: {str(e)}"


# ==============================
# 🔐 Estado da Sessão
# ==============================
if 'chunks' not in st.session_state:
    st.session_state.chunks = []
if 'embeddings' not in st.session_state:
    st.session_state.embeddings = []
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []
if 'processed' not in st.session_state:
    st.session_state.processed = False

# ==============================
# 🧩 Processamento dos PDFs
# ==============================
if uploaded_files and api_key:
    if not st.session_state.processed:
        with st.spinner("📖 Processando PDFs..."):
            try:
                # Configurar cliente OpenAI - CORREÇÃO AQUI
                client = OpenAI(api_key=api_key)
                
                # Extrair texto
                raw_text = extract_text_from_pdfs(uploaded_files)

                if raw_text.strip():
                    # Dividir em chunks
                    st.session_state.chunks = split_text_into_chunks(raw_text)
                    
                    # Criar embeddings
                    progress_bar = st.progress(0)
                    embeddings = []
                    
                    for i, chunk in enumerate(st.session_state.chunks):
                        embedding = get_embedding(chunk, client)
                        if embedding:
                            embeddings.append(embedding)
                        progress_bar.progress((i + 1) / len(st.session_state.chunks))
                    
                    st.session_state.embeddings = embeddings
                    st.session_state.processed = True
                    st.session_state.client = client
                    
                    st.success(f"✅ {len(uploaded_files)} arquivo(s) processado(s) com sucesso!")
                    st.info(f"📊 {len(st.session_state.chunks)} segmentos de texto criados")
                else:
                    st.error("❌ Não foi possível extrair texto dos PDFs.")
            except Exception as e:
                st.error(f"Erro ao processar PDFs: {str(e)}")

# ==============================
# 💬 Interface de Chat
# ==============================
if st.session_state.processed:
    st.markdown("---")
    st.header("💬 Chat Inteligente")

    # Histórico
    for msg in st.session_state.chat_history:
        with st.chat_message(msg["role"]):
            st.write(msg["content"])

    # Entrada do usuário
    if user_question := st.chat_input("Faça sua pergunta sobre o conteúdo dos PDFs..."):
        st.session_state.chat_history.append({"role": "user", "content": user_question})
        with st.chat_message("user"):
            st.write(user_question)

        with st.chat_message("assistant"):
            with st.spinner("Pensando..."):
                try:
                    # Encontrar chunks relevantes
                    relevant_chunks = find_relevant_chunks(
                        user_question,
                        st.session_state.chunks,
                        st.session_state.embeddings,
                        st.session_state.client
                    )
                    
                    # Criar contexto
                    context = "\n\n".join(relevant_chunks)
                    
                    # Gerar resposta
                    answer = generate_answer(
                        user_question,
                        context,
                        st.session_state.chat_history,
                        st.session_state.client
                    )
                    
                    st.write(answer)
                    st.session_state.chat_history.append({"role": "assistant", "content": answer})

                    # Mostrar fontes
                    with st.expander("📄 Trechos relevantes consultados"):
                        for i, chunk in enumerate(relevant_chunks):
                            st.markdown(f"**Trecho {i+1}:**")
                            st.text(chunk[:400] + "...")
                            st.markdown("---")
                            
                except Exception as e:
                    st.error(f"Erro ao processar pergunta: {str(e)}")
else:
    st.info("👆 Faça upload dos PDFs e insira sua API Key na barra lateral para começar!")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("### 📚 Passo 1\nEnvie seus PDFs sobre mercado financeiro")
    with col2:
        st.markdown("### 🔑 Passo 2\nInsira sua OpenAI API Key")
    with col3:
        st.markdown("### 💬 Passo 3\nFaça perguntas e obtenha respostas!")

# ==============================
# 🦾 Rodapé
# ==============================
st.markdown("---")
st.markdown("""
<div style='text-align: center'>
    <p>Desenvolvido com ❤️ usando OpenAI e Streamlit</p>
</div>
""", unsafe_allow_html=True)