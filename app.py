import pymongo
from flask import Flask, render_template, abort

app = Flask(__name__)

try:
    conn = pymongo.MongoClient("mongodb://localhost:27017/", serverSelectionTimeoutMS=2000)
    banco = conn["pokemon"]
    colecao = banco["kanto"]
    
    conn.server_info() 
    db_disponivel = True
    print("Conexão com MongoDB estabelecida com sucesso!")
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
            print(f"Erro ao buscar lista de pokemons: {e}")

    if not pokemons:
        pokemons = [
            {"Nome": "Pikachu", "Numero": 25, "Imagem": "025.png", "TipoPrimario": "Elétrico"},
            {"Nome": "Bulbasaur", "Numero": 1, "Imagem": "001.png", "TipoPrimario": "Grama"}
        ]

    return render_template("index.html", pokemons=pokemons)

@app.route("/pokemon/<nome>")
def detalhes(nome):
    if not db_disponivel:
        return "Erro: Banco de dados não conectado.", 500
    
    pokemon = colecao.find_one({"Nome": nome})
    
    if pokemon:
        return render_template("detalhes.html", pokemon=pokemon)
    else:
        abort(404, description="Pokémon não registrado.")

if __name__ == "__main__":
    app.run(debug=True)