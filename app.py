import os
import pymongo
from flask import Flask, render_template

# 1. Definição ÚNICA do app
app = Flask(__name__, template_folder='templates', static_folder='static')

# 2. Configuração do MongoDB (com tratamento de erro para a Vercel)
MONGO_URI = os.environ.get("MONGODB_URI", "mongodb://localhost:27017/")

try:
    # Timeout de 2s para não travar o deploy da Vercel
    conn = pymongo.MongoClient(MONGO_URI, serverSelectionTimeoutMS=2000)
    banco = conn["pokemon"]
    colecao = banco["kanto"]
    
    # Testa a conexão
    conn.server_info()
    db_disponivel = True
except Exception as e:
    print(f"Aviso: Rodando sem MongoDB (Localhost inacessível na nuvem). Erro: {e}")
    db_disponivel = False

@app.route("/")
def index():
    if db_disponivel:
        pokemons = list(colecao.find())
    else:
        # POKEMONS DE TESTE: Para você ver o layout na Vercel mesmo sem banco
        pokemons = [
            {"name": "Pikachu (Teste)", "numero": 25},
            {"name": "Bulbasaur (Teste)", "numero": 1}
        ]

    # Garante que o número apareça no card
    for i, p in enumerate(pokemons):
        if "numero" not in p:
            p["numero"] = i + 1

    return render_template("index.html", pokemons=pokemons)

# 3. Rodar localmente
if __name__ == "__main__":
    app.run(debug=True)