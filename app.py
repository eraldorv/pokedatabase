from flask import Flask, render_template
import pymongo

app = Flask(__name__)

conn = pymongo.MongoClient("mongodb://localhost:27017/")

banco = conn["pokemon"]
colecao = banco["kanto"]

@app.route("/")
def index():

    pokemons = list(colecao.find())

    # adicionar índice numérico
    for i, p in enumerate(pokemons):
        p["numero"] = i + 1

    return render_template(
        "index.html",
        pokemons=pokemons
    )

if __name__ == "__main__":
    app.run(debug=True)