import os
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import joblib

# ===============================
# CONFIGURAÇÕES E CAMINHOS
# ===============================
BASE_DIR = os.path.dirname(__file__)
DATA_PATH = os.path.join(BASE_DIR, '../data/dados_vendas.csv')
MODEL_PATH = os.path.join(BASE_DIR, '../models/modelo_vendas.pkl')

# ===============================
# ETAPA 1: CARREGAR DADOS
# ===============================
if not os.path.exists(DATA_PATH):
    raise FileNotFoundError(f"❌ Arquivo de dados não encontrado em: {DATA_PATH}")

df = pd.read_csv(DATA_PATH)

if not {'temperatura', 'umidade', 'feriado', 'vendas'}.issubset(df.columns):
    raise ValueError("❌ O arquivo CSV precisa conter as colunas: temperatura, umidade, feriado, vendas")

print(f"📊 Dados carregados com sucesso! Total de registros: {len(df)}")

# ===============================
# ETAPA 2: SEPARAR VARIÁVEIS
# ===============================
X = df[['temperatura', 'umidade', 'feriado']]
y = df['vendas']

# ===============================
# ETAPA 3: DIVIDIR TREINO/TESTE
# ===============================
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# ===============================
# ETAPA 4: TREINAR MODELO
# ===============================
modelo = LinearRegression()
modelo.fit(X_train, y_train)

# ===============================
# ETAPA 5: AVALIAR MODELO
# ===============================
score = modelo.score(X_test, y_test)
print(f"📈 Acurácia (R²): {score:.2f}")

# ===============================
# ETAPA 6: SALVAR MODELO
# ===============================
os.makedirs(os.path.dirname(MODEL_PATH), exist_ok=True)
joblib.dump(modelo, MODEL_PATH)
print(f"✅ Modelo salvo em: {MODEL_PATH}")
