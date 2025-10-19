# 🍦 Previsão de Vendas de Sorvete — Projeto DIO

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-API-lightgrey.svg)](https://flask.palletsprojects.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Machine Learning](https://img.shields.io/badge/Machine%20Learning-Regression-brightgreen.svg)]()
[![DIO](https://img.shields.io/badge/DIO-Projeto%20Educacional-purple.svg)](https://www.dio.me)

---

### 👨‍💻 Autor  
**Edson Gomes**  
📧 **E-mail:** [edsgom@gmail.com](mailto:edsgom@gmail.com)  
🌐 **GitHub:** [github.com/edsongom1](https://github.com/edsongom1)  
💼 **LinkedIn:** [linkedin.com/in/edsongom](https://www.linkedin.com/in/edsongom)  

---

## 📖 Sobre o Projeto

Este projeto foi desenvolvido como parte de um **desafio DIO**, e demonstra um pipeline completo de **Machine Learning + Flask API**.  
Ele prevê o número de **vendas de sorvete** com base em **temperatura, umidade e se é feriado**, utilizando um modelo simples de **Regressão Linear**.

---

## 🎯 Objetivos

- Aplicar conceitos de **aprendizado supervisionado** (regressão linear).  
- Treinar um modelo com **dados históricos simulados**.  
- Servir o modelo em uma **API Flask**.  
- Criar uma **interface web interativa** (HTML + JS) para prever vendas diretamente no navegador.  

---

## 🧩 Estrutura Geral do Projeto

```bash
dp-100/
│
├── data/
│   └── dados_vendas.csv           # Dados de entrada (temperatura, umidade, feriado, vendas)
│
├── models/
│   └── modelo_vendas.pkl          # Modelo treinado (gerado pelo treinar.py)
│
├── app/
│   ├── main.py                    # Aplicação Flask + interface web
│   └── treinar.py                 # Script de treinamento do modelo
│
├── requirements.txt               # Dependências do projeto
└── README.md                      # Documentação do projeto
```

---

## 🧠 O que o Projeto Faz

| Etapa | Arquivo | Descrição |
|-------|----------|------------|
| **Treinamento** | `treinar.py` | Treina um modelo de regressão linear com base nos dados CSV |
| **Serialização** | `modelo_vendas.pkl` | Salva o modelo treinado no formato binário |
| **Serviço Web** | `main.py` | Cria servidor Flask com `/` (formulário) e `/predict` (API) |
| **Interface** | HTML + JS embutidos no Flask | Permite testar previsões direto no navegador |

---

## 🧾 Requisitos

- Python **3.8+** (recomendado: 3.10 ou superior)
- Pip (instalador de pacotes Python)

Instale as dependências com:

```bash
pip install -r requirements.txt
```

📦 **Dependências principais**
```
flask
scikit-learn
pandas
numpy
joblib
mlflow
matplotlib
```

---

## ⚙️ Instalação Passo a Passo

1️⃣ **Clone o repositório:**
```bash
git clone https://github.com/edsongom1/<nome-do-repositorio>.git
cd <nome-do-repositorio>
```

2️⃣ **Crie e ative um ambiente virtual (recomendado):**
```bash
python -m venv .venv
# Windows
.venv\Scripts\activate
# Linux/Mac
source .venv/bin/activate
```

3️⃣ **Instale as dependências:**
```bash
pip install -r requirements.txt
```

4️⃣ **Verifique se existe o arquivo de dados:**
```
data/dados_vendas.csv
```
Se não existir, veja abaixo como **gerar dados fictícios**.

---

## 🧩 Geração de Dados de Exemplo (opcional)

Se quiser testar do zero, crie dados simulados:

```python
import pandas as pd
import numpy as np, os

N = 1000
np.random.seed(42)
temperatura = np.random.normal(25, 5, N).round(1)
umidade = np.random.normal(60, 10, N).round(1)
feriado = np.random.choice([0,1], N, p=[0.85,0.15])
vendas = (temperatura*5) - (umidade*0.5) + (feriado*20) + np.random.normal(0,10,N)
vendas = np.clip(vendas, 0, None).round().astype(int)
df = pd.DataFrame({'temperatura':temperatura,'umidade':umidade,'feriado':feriado,'vendas':vendas})
os.makedirs('data', exist_ok=True)
df.to_csv('data/dados_vendas.csv', index=False)
print('✅ CSV gerado com sucesso!')
```

Execute:
```bash
python gerar_dados.py
```

---

## 🧠 Treinando o Modelo

Arquivo: `app/treinar.py`

Etapas do script:

1. Carrega os dados de `data/dados_vendas.csv`  
2. Separa features (`temperatura`, `umidade`, `feriado`) e alvo (`vendas`)  
3. Divide treino/teste  
4. Treina o modelo `LinearRegression()`  
5. Exibe o **R² (acurácia)**  
6. Salva o modelo como `models/modelo_vendas.pkl`

Execute:
```bash
python app/treinar.py
```

Saída esperada:
```
📊 Dados carregados com sucesso! Total de registros: 1000
📈 Acurácia (R²): 0.92
✅ Modelo salvo em: models/modelo_vendas.pkl
```

---

## 🌐 Executando a Aplicação Flask

Após treinar o modelo:

```bash
python app/main.py
```

Abra no navegador:  
👉 [http://127.0.0.1:5000/](http://127.0.0.1:5000/)

### Interface Web
Você verá um formulário interativo:
- **Temperatura (°C)**
- **Umidade (%)**
- **Feriado (0 = Não / 1 = Sim)**  
Clique em **Prever Vendas** → resultado aparece na tela.

---

## 🔬 Testando via API (curl/Postman)

### Endpoint `/predict`
Método: `POST`  
URL: `http://127.0.0.1:5000/predict`

Corpo JSON:
```json
{
  "temperatura": 30,
  "umidade": 50,
  "feriado": 1
}
```

### Exemplo com curl:
```bash
curl -X POST http://127.0.0.1:5000/predict \
-H "Content-Type: application/json" \
-d "{\"temperatura\":30, \"umidade\":50, \"feriado\":1}"
```

### Resposta esperada:
```json
{
  "entrada": {"temperatura": 30, "umidade": 50, "feriado": 1},
  "previsao_vendas": 245.67
}
```

---

## 🧱 Estrutura Técnica do Modelo

- **Tipo:** Regressão Linear  
- **Biblioteca:** scikit-learn  
- **Input:** `[temperatura, umidade, feriado]`  
- **Output:** valor numérico (vendas previstas)  
- **Persistência:** `joblib.dump()` / `joblib.load()`  

---

## 🚨 Possíveis Problemas

| Erro | Causa | Solução |
|------|--------|----------|
| `FileNotFoundError: modelo_vendas.pkl` | Modelo não foi treinado | Execute `python app/treinar.py` |
| `ValueError: missing keys` | JSON incorreto | Verifique se enviou `temperatura`, `umidade`, `feriado` |
| `MemoryError` | Flask reloader ativo no Windows | Rode com `debug=False, use_reloader=False` |
| `ModuleNotFoundError` | Dependências ausentes | Rode `pip install -r requirements.txt` |

---

## 🔒 Boas Práticas e Deploy

- O servidor embutido do Flask é apenas para desenvolvimento.  
- Para produção, use **Gunicorn**, **uWSGI** ou plataformas como:
  - Azure App Service  
  - Render  
  - Railway  
  - Heroku  
- Adicione logs e autenticação se for expor publicamente.  

---

## 🚀 Melhorias Futuras

- Adicionar **gráficos interativos (Plotly)**.  
- Criar **dashboard histórico de previsões**.  
- Dockerizar o projeto.  
- Automatizar re-treinamento com dados novos.  
- Implementar **autenticação e controle de acesso**.  
- Adicionar **testes unitários e CI/CD**.  

---

## 🪪 Licença

Este projeto é licenciado sob a licença **MIT**.  
Sinta-se livre para estudar, modificar e usar para fins educacionais.

---

## 📬 Contato

📧 **Email:** [edsgom@gmail.com](mailto:edsgom@gmail.com)  
🌐 **GitHub:** [github.com/edsongom1](https://github.com/edsongom1)  
💼 **LinkedIn:** [linkedin.com/in/edsongom](https://www.linkedin.com/in/edsongom)

---

> Desenvolvido com 💙 por **Edson Gomes** para o desafio **Digital Innovation One (DIO)**.  
> Projeto educacional demonstrando **Machine Learning aplicado com Flask**.
#
