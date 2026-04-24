import pymongo

# 1. CONEXÃO
try:
    conn = pymongo.MongoClient("mongodb://localhost:27017/", serverSelectionTimeoutMS=2000)
    banco = conn["pokemon"]
    colecao = banco["kanto"]
    conn.server_info()
    print("Conexão com MongoDB estabelecida!")
except Exception as e:
    print(f"Erro ao conectar: {e}")
    exit()

colecao.delete_many({})
print("Registros antigos removidos!")

colecao.create_index("Numero", unique=True)
colecao.create_index("Nome", unique=True)

print("Lendo pokedex...")
pokemons_lista = [
    {
        "Numero": 1, "Nome": "Bulbasaur", "TipoPrimario": "Grama", "TipoSecundario": "Veneno",
        "Imagem": "001.png", "Altura": "0.7 m", "Peso": "6.9 kg", "descoberto": False,
        "Descricao": "Uma semente estranha foi plantada em suas costas no nascimento."
    },
    {
        "Numero": 2, "Nome": "Ivysaur", "TipoPrimario": "Grama", "TipoSecundario": "Veneno",
        "Imagem": "002.png", "Altura": "1.0 m", "Peso": "13.0 kg", "descoberto": False,
        "Descricao": "Quando o bulbo em suas costas cresce, parece perder a mobilidade."
    },
    {
        "Numero": 3, "Nome": "Venusaur", "TipoPrimario": "Grama", "TipoSecundario": "Veneno",
        "Imagem": "003.png", "Altura": "2.0 m", "Peso": "100.0 kg", "descoberto": False,
        "Descricao": "A planta floresce absorvendo energia solar."
    },
    {
        "Numero": 4, "Nome": "Charmander", "TipoPrimario": "Fogo", "TipoSecundario": "Nenhum",
        "Imagem": "004.png", "Altura": "0.6 m", "Peso": "8.5 kg", "descoberto": False,
        "Descricao": "Prefere lugares quentes. O vapor jorra da ponta de sua cauda."
    },
    {
        "Numero": 5, "Nome": "Charmeleon", "TipoPrimario": "Fogo", "TipoSecundario": "Nenhum",
        "Imagem": "005.png", "Altura": "1.1 m", "Peso": "19.0 kg", "descoberto": False,
        "Descricao": "Quando balança sua cauda em chamas, eleva a temperatura ao redor."
    },
    {
        "Numero": 6, "Nome": "Charizard", "TipoPrimario": "Fogo", "TipoSecundario": "Voador",
        "Imagem": "006.png", "Altura": "1.7 m", "Peso": "90.5 kg", "descoberto": False,
        "Descricao": "Cospe fogo que é quente o suficiente para derreter rochas."
    },
    {
        "Numero": 7, "Nome": "Squirtle", "TipoPrimario": "Água", "TipoSecundario": "Nenhum",
        "Imagem": "007.png", "Altura": "0.5 m", "Peso": "9.0 kg", "descoberto": False,
        "Descricao": "Após o nascimento, suas costas incham e endurecem formando um casco."
    },
    {
        "Numero": 8, "Nome": "Wartortle", "TipoPrimario": "Água", "TipoSecundario": "Nenhum",
        "Imagem": "008.png", "Altura": "1.0 m", "Peso": "22.5 kg", "descoberto": False,
        "Descricao": "Muitas vezes se esconde na água para vigiar presas incautas."
    },
    {
        "Numero": 9, "Nome": "Blastoise", "TipoPrimario": "Água", "TipoSecundario": "Nenhum",
        "Imagem": "009.png", "Altura": "1.6 m", "Peso": "85.5 kg", "descoberto": False,
        "Descricao": "Um Pokémon brutal com jatos de água pressurizada em seu casco."
    }
]
colecao.insert_many(pokemons_lista)

caterpie = {
    "Numero": 10, "Nome": "Caterpie", "TipoPrimario": "Inseto", "TipoSecundario": "Nenhum",
    "Imagem": "010.png", "Altura": "0.3 m", "Peso": "2.9 kg", "descoberto": False,
    "Descricao": "Suas pernas curtas são cobertas com ventosas para escalar."
}
colecao.insert_one(caterpie)
print("Pokemon inseridos com sucesso!")

print("Lendo Pokedex atualizada:")
for pokemon in colecao.find().sort("Numero", 1):
    print(f"#{pokemon['Numero']} - {pokemon['Nome']}")

print("Removendo Caterpie para demonstração...")
resultado = colecao.delete_one({"Nome": "Caterpie"})
if resultado.deleted_count > 0:
    print("Caterpie removido!")

colecao.insert_one(caterpie)
print("Pokedex atualizada, Caterpie registrado como #10 na pokedex.")

conn.close()