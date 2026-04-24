from flask import Flask, render_template
import pymongo
import os

app = Flask(__name__)

# Configuração da conexão com o Banco de Dados
# Se estiver na Vercel, ele tentará pegar uma variável de ambiente. 
# Se não encontrar, usa o localhost.
MONGO_URI = os.environ.get("MONGODB_URI", "mongodb://localhost:27017/")

try:
    # Definimos um timeout curto (2 segundos) para não travar o site se o banco estiver offline
    conn = pymongo.MongoClient(MONGO_URI, serverSelectionTimeoutMS=2000)
    banco = conn["pokemon"]
    colecao = banco["kanto"]
    
    # Testamos a conexão rápida
    conn.server_info()
    db_disponivel = True
except Exception as e:
    print(f"Erro ao conectar ao MongoDB: {e}")
    db_disponivel = False

@app.route("/")
def index():
    if db_disponivel:
        # Busca os pokemons no banco
        pokemons = list(colecao.find())
    else:
        # Se o banco falhar (como acontece na Vercel sem o MongoDB Atlas),
        # criamos uma lista vazia ou com dados de exemplo para o site não cair.
        pokemons = []
        print("Aviso: Exibindo página sem dados do banco (banco offline).")

    # Adicionar índice numérico para os cards
    for i, p in enumerate(pokemons):
        p["numero"] = i + 1

    return render_template(
        "index.html",
        pokemons=pokemons
    )

# Para rodar localmente
if __name__ == "__main__":
    app.run(debug=True)