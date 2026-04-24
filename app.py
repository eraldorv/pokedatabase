import os
import pymongo
from flask import Flask, render_template

app = Flask(__name__)

# Tenta pegar a URL do banco, se não existir, usa None
MONGO_URI = os.environ.get("MONGODB_URI")

db_disponivel = False
colecao = None

if MONGO_URI:
    try:
        conn = pymongo.MongoClient(MONGO_URI, serverSelectionTimeoutMS=2000)
        banco = conn["pokemon"]
        colecao = banco["kanto"]
        conn.server_info()
        db_disponivel = True
    except:
        db_disponivel = False
else:
    # Se estiver no seu PC (local), tenta o localhost
    try:
        conn = pymongo.MongoClient("mongodb://localhost:27017/", serverSelectionTimeoutMS=1000)
        banco = conn["pokemon"]
        colecao = banco["kanto"]
        db_disponivel = True
    except:
        db_disponivel = False

@app.route("/")
def index():
    pokemons = []
    if db_disponivel and colecao is not None:
        try:
            pokemons = list(colecao.find())
        except:
            pass
            
    if not pokemons:
        # Dados de backup para o site nunca dar erro 500
        pokemons = [
            {"name": "Pikachu", "numero": 25},
            {"name": "Bulbasaur", "numero": 1}
        ]

    for i, p in enumerate(pokemons):
        if "numero" not in p:
            p["numero"] = i + 1

    return render_template("index.html", pokemons=pokemons)