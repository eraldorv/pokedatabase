import pymongo
from flask import Flask, render_template

app = Flask(__name__)

try:
    conn = pymongo.MongoClient("mongodb://localhost:27017/")
    banco = conn["pokemon"]
    colecao = banco["kanto"]
    conn.server_info() 
    db_disponivel = True
except Exception as e:
    print(f"Erro ao conectar ao MongoDB local: {e}")
    db_disponivel = False

@app.route("/")
def index():
    pokemons = []
    
    if db_disponivel:
        try:
            pokemons = list(colecao.find())
        except Exception as e:
            print(f"Erro ao buscar dados: {e}")

    if not pokemons:
        pokemons = [
            {"name": "Pikachu (Backup)", "numero": 25},
            {"name": "Bulbasaur (Backup)", "numero": 1}
        ]

    for i, p in enumerate(pokemons):
        if "numero" not in p:
            p["numero"] = i + 1

    return render_template("index.html", pokemons=pokemons)

if __name__ == "__main__":
    app.run(debug=True)