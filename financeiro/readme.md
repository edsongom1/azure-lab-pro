# 📊 Sistema de Busca Inteligente para PDFs - Mercado Financeiro

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-1.39.0-red.svg)
![OpenAI](https://img.shields.io/badge/OpenAI-GPT--4-green.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

> Sistema inteligente de análise de documentos PDF sobre mercado financeiro, utilizando IA (GPT-4) e embeddings para busca semântica avançada.

## 📋 Sobre o Projeto

Este projeto foi desenvolvido como parte do desafio da **[DIO.me](https://dio.me)** e implementa um assistente de IA capaz de ler, processar e responder perguntas sobre múltiplos documentos PDF relacionados ao mercado financeiro. O sistema utiliza técnicas avançadas de processamento de linguagem natural (NLP) e busca vetorial para encontrar informações relevantes e gerar respostas contextualizadas.

### 🎯 Funcionalidades Principais

- **📄 Upload Múltiplo de PDFs**: Carregue vários documentos simultaneamente
- **🧠 Busca Semântica Inteligente**: Utiliza embeddings da OpenAI para encontrar conteúdo relevante
- **💬 Chat Interativo**: Interface conversacional com histórico de mensagens
- **🔍 Contexto Preciso**: Mostra os trechos dos documentos utilizados para gerar cada resposta
- **⚡ Processamento Eficiente**: Divisão de texto em chunks com overlap para melhor precisão

## 🚀 Tecnologias Utilizadas

### Core
- **[Python 3.8+](https://www.python.org/)** - Linguagem de programação
- **[Streamlit 1.39.0](https://streamlit.io/)** - Framework para interface web
- **[OpenAI API](https://openai.com/)** - GPT-4 para geração de respostas e embeddings

### Bibliotecas Principais
- **PyPDF2** - Extração de texto de arquivos PDF
- **LangChain** - Framework para aplicações com LLMs
- **FAISS** - Biblioteca para busca vetorial eficiente
- **NumPy** - Computação numérica
- **scikit-learn** - Cálculo de similaridade de cosseno

### IA e NLP
- **text-embedding-3-small** - Modelo de embeddings da OpenAI
- **GPT-4o-mini** - Modelo de linguagem para geração de respostas
- **TensorFlow/Keras** - Suporte para transformers

## 📦 Instalação

### Pré-requisitos

- Python 3.8 ou superior
- Conta na OpenAI com API Key ativa
- pip (gerenciador de pacotes Python)

### Passo a Passo

1. **Clone o repositório**
```bash
git clone https://github.com/edsongom1/sistema-busca-pdf.git
cd sistema-busca-pdf
```

2. **Crie um ambiente virtual (recomendado)**
```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Linux/Mac
source venv/bin/activate
```

3. **Instale as dependências**
```bash
pip install -r requeriments.txt
```

4. **Configure sua API Key da OpenAI**
   - Obtenha sua chave em: https://platform.openai.com/api-keys
   - A chave será inserida diretamente na interface do aplicativo

5. **Execute o aplicativo**
```bash
streamlit run app1.py
```

6. **Acesse no navegador**
   - O aplicativo abrirá automaticamente em: `http://localhost:8501`

## 💻 Como Usar

### 1️⃣ Configuração Inicial
- Na barra lateral, insira sua **OpenAI API Key**
- Faça upload de um ou mais arquivos PDF sobre mercado financeiro

### 2️⃣ Processamento
- Aguarde o processamento dos documentos
- O sistema criará embeddings para busca semântica

### 3️⃣ Interação
- Digite suas perguntas no chat
- Receba respostas contextualizadas baseadas nos PDFs
- Visualize os trechos relevantes consultados

### 📝 Exemplos de Perguntas

```
- Qual foi o impacto da taxa Selic no mercado?
- Como funciona a alocação de ativos?
- Quais são as principais tendências do mercado financeiro?
- O que dizem os documentos sobre renda fixa?
- Explique a estratégia de diversificação mencionada
```

## 🏗️ Arquitetura do Sistema

```
┌─────────────────┐
│  Upload PDFs    │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ Extração Texto  │
│   (PyPDF2)      │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ Divisão Chunks  │
│ (overlap 200)   │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│   Embeddings    │
│    (OpenAI)     │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ Busca Vetorial  │
│  (Cosine Sim)   │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  GPT-4 Answer   │
│  (Contextual)   │
└─────────────────┘
```

## 📂 Estrutura de Arquivos

```
sistema-busca-pdf/
│
├── app1.py                 # Aplicação principal Streamlit
├── requeriments.txt        # Dependências do projeto
├── README.md              # Este arquivo
└── .gitignore             # Arquivos ignorados pelo Git
```

## ⚙️ Configurações Avançadas

### Parâmetros de Chunking
```python
chunk_size = 1000    # Tamanho de cada segmento de texto
overlap = 200        # Sobreposição entre chunks
```

### Busca Semântica
```python
top_k = 3           # Número de chunks mais relevantes
```

### Modelo GPT
```python
model = "gpt-4o-mini"
temperature = 0.7
max_tokens = 1000
```

## 🔒 Segurança

- **API Key**: Nunca compartilhe sua chave da OpenAI
- **Tipo Password**: A chave é inserida como campo de senha na interface
- **Session State**: Dados armazenados apenas durante a sessão

## 🤝 Contribuindo

Contribuições são bem-vindas! Para contribuir:

1. Faça um Fork do projeto
2. Crie uma branch para sua feature (`git checkout -b feature/NovaFuncionalidade`)
3. Commit suas mudanças (`git commit -m 'Adiciona nova funcionalidade'`)
4. Push para a branch (`git push origin feature/NovaFuncionalidade`)
5. Abra um Pull Request

## 🐛 Problemas Conhecidos

- PDFs com imagens podem não extrair texto corretamente
- Documentos muito grandes podem levar mais tempo para processar
- Requer conexão com a internet para acessar a API da OpenAI

## 📈 Melhorias Futuras

- [ ] Suporte para outros formatos (DOCX, TXT)
- [ ] Cache de embeddings para otimização
- [ ] Exportação de conversas
- [ ] Suporte multilíngue
- [ ] Interface para upload de múltiplos tipos de documentos
- [ ] Integração com outras LLMs (Anthropic Claude, Google Gemini)

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.

## 👨‍💻 Autor

**Edson Gomes**

- 📧 Email: edsgom@gmail.com
- 💼 LinkedIn: [linkedin.com/in/edsongom](https://linkedin.com/in/edsongom)
- 🐙 GitHub: [github.com/edsongom1](https://github.com/edsongom1)

## 🎓 Agradecimentos

- **[DIO.me](https://dio.me)** - Pela oportunidade e desafio proposto
- **OpenAI** - Pela API poderosa de IA
- **Streamlit** - Por facilitar a criação de interfaces web
- Comunidade Python - Pelo suporte e bibliotecas incríveis

---

<div align="center">

**Desenvolvido com ❤️ para o desafio DIO.me**

⭐ Se este projeto foi útil, deixe uma estrela no repositório!

</div>