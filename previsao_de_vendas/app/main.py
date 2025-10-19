from flask import Flask, request, jsonify, render_template_string
import numpy as np
import joblib
import os

# ===============================
# CONFIGURAÇÃO DO FLASK
# ===============================
app = Flask(__name__)

# Caminho do modelo
MODEL_PATH = os.path.join(os.path.dirname(__file__), '../models/modelo_vendas.pkl')

# ===============================
# CARREGAR MODELO
# ===============================
if not os.path.exists(MODEL_PATH):
    raise FileNotFoundError(f"❌ Modelo não encontrado em: {MODEL_PATH}. Execute 'treinar.py' primeiro.")

try:
    model = joblib.load(MODEL_PATH)
    print(f"✅ Modelo carregado com sucesso de: {MODEL_PATH}")
except Exception as e:
    raise RuntimeError(f"Erro ao carregar o modelo: {e}")

# ===============================
# ROTA PRINCIPAL
# ===============================
@app.route('/')
def home():
    html = """
    <h2>🍦 Previsão de Vendas de Sorvete</h2>
    <p>Use o endpoint <b>/predict</b> com método POST para prever as vendas.</p>
    <p>Exemplo de JSON:</p>
    <pre>{
  "temperatura": 30,
  "umidade": 50,
  "feriado": 1
}</pre>
    """
    return render_template_string(html)

# ===============================
# ENDPOINT DE PREVISÃO
# ===============================
@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()

        # Validação de entrada
        if not all(k in data for k in ['temperatura', 'umidade', 'feriado']):
            return jsonify({"erro": "Parâmetros necessários: temperatura, umidade, feriado"}), 400

        # Converter entrada em array numpy
        X_input = np.array([[data['temperatura'], data['umidade'], data['feriado']]])

        # Fazer previsão
        pred = model.predict(X_input)[0]

        return jsonify({
            "entrada": data,
            "previsao_vendas": round(float(pred), 2)
        })
    except Exception as e:
        return jsonify({"erro": str(e)}), 500

# ===============================
# FAVICON (opcional)
# ===============================
@app.route('/favicon.ico')
def favicon():
    return '', 204

# ===============================
# EXECUTAR SERVIDOR
# ===============================
if __name__ == '__main__':
    app.run(debug=False, use_reloader=False)
