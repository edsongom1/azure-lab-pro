import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import mlflow
import mlflow.sklearn
import matplotlib.pyplot as plt
import pickle
import os

# Caminhos
base_path = os.path.dirname(__file__)
data_path = os.path.join(base_path, "../inputs/dados_vendas.csv")
model_path = os.path.join(base_path, "../models/modelo_vendas.pkl")

# 1. Carregar dados
data = pd.read_csv(data_path)
X = data[['temperatura']]
y = data['vendas']

# 2. Treinar modelo
model = LinearRegression()
model.fit(X, y)

# 3. Fazer previsões
y_pred = model.predict(X)

# 4. Avaliar modelo
mse = mean_squared_error(y, y_pred)
r2 = r2_score(y, y_pred)
print(f"MSE: {mse:.2f}")
print(f"R²: {r2:.2f}")

# 5. Visualização
plt.scatter(X, y, color='blue')
plt.plot(X, y_pred, color='red')
plt.title("Previsão de Vendas de Sorvete vs Temperatura")
plt.xlabel("Temperatura (°C)")
plt.ylabel("Vendas")
plt.show()

# 6. Log com MLflow
mlflow.set_experiment("gelato_magico_vendas")
with mlflow.start_run():
    mlflow.log_param("modelo", "LinearRegression")
    mlflow.log_metric("mse", mse)
    mlflow.log_metric("r2", r2)
    mlflow.sklearn.log_model(model, "modelo_vendas")

# 7. Salvar modelo
os.makedirs(os.path.dirname(model_path), exist_ok=True)
with open(model_path, "wb") as f:
    pickle.dump(model, f)

print(f"✅ Modelo salvo em: {model_path}")
