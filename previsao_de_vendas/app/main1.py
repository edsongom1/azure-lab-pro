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
# INTERFACE WEB (HTML)
# ===============================
@app.route('/')
def home():
    html = """
    <!DOCTYPE html>
    <html lang="pt-br">
    <head>
        <meta charset="UTF-8">
        <title>🍦 Previsão de Vendas de Sorvete</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                background: #f8fafc;
                color: #333;
                display: flex;
                flex-direction: column;
                align-items: center;
                justify-content: center;
                height: 100vh;
            }
            h2 {
                color: #2c3e50;
                font-size: 26px;
            }
            form {
                background: #fff;
                padding: 20px 30px;
                border-radius: 12px;
                box-shadow: 0 4px 10px rgba(0,0,0,0.1);
                width: 320px;
                text-align: left;
            }
            label {
                font-weight: bold;
                display: block;
                margin-top: 10px;
            }
            input {
                width: 100%;
                padding: 8px;
                margin-top: 5px;
                border: 1px solid #ccc;
                border-radius: 6px;
            }
            button {
                margin-top: 15px;
                width: 100%;
                padding: 10px;
                background: #3498db;
                color: white;
                border: none;
                border-radius: 6px;
                font-weight: bold;
                cursor: pointer;
                transition: 0.2s;
            }
            button:hover {
                background: #2980b9;
            }
            .resultado {
                margin-top: 20px;
                font-size: 18px;
                text-align: center;
            }
        </style>
    </head>
    <body>
        <h2>🍦 Previsão de Vendas de Sorvete</h2>
        <form id="form">
            <label>Temperatura (°C)</label>
            <input type="number" id="temperatura" step="0.1" required>

            <label>Umidade (%)</label>
            <input type="number" id="umidade" step="0.1" required>

            <label>Feriado (0 = Não, 1 = Sim)</label>
            <input type="number" id="feriado" min="0" max="1" required>

            <button type="submit">Prever Vendas</button>
        </form>

        <div class="resultado" id="resultado"></div>

        <script>
            document.getElementById('form').addEventListener('submit', async (e) => {
                e.preventDefault();
                const temperatura = parseFloat(document.getElementById('temperatura').value);
                const umidade = parseFloat(document.getElementById('umidade').value);
                const feriado = parseInt(document.getElementById('feriado').value);

                const resposta = await fetch('/predict', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ temperatura, umidade, feriado })
                });

                const dados = await resposta.json();
                const resultadoDiv = document.getElementById('resultado');

                if (dados.previsao_vendas) {
                    resultadoDiv.innerHTML = `📈 Previsão de Vendas: <b>${dados.previsao_vendas}</b>`;
                } else {
                    resultadoDiv.innerHTML = `❌ Erro: ${dados.erro || 'Não foi possível gerar a previsão.'}`;
                }
            });
        </script>
    </body>
    </html>
    """
    return render_template_string(html)

# ===============================
# ENDPOINT DE PREVISÃO
# ===============================
@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        if not all(k in data for k in ['temperatura', 'umidade', 'feriado']):
            return jsonify({"erro": "Parâmetros necessários: temperatura, umidade, feriado"}), 400

        X_input = np.array([[data['temperatura'], data['umidade'], data['feriado']]])
        pred = model.predict(X_input)[0]

        return jsonify({
            "entrada": data,
            "previsao_vendas": round(float(pred), 2)
        })
    except Exception as e:
        return jsonify({"erro": str(e)}), 500

# ===============================
# EXECUTAR SERVIDOR
# ===============================
if __name__ == '__main__':
    app.run(debug=False, use_reloader=False)
