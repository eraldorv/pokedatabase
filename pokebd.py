import pymongo

conn = pymongo.MongoClient("mongodb://localhost:27017/")

# criando banco
banco = conn["pokemon"]

# criando colecao
colecao = banco["kanto"]

# criar índice único
colecao.create_index("Nome", unique=True)

# apagar registros antigos
colecao.delete_many({})

print("Pokemons antigos removidos!")

# inserir pokemons com numero
colecao.insert_many([

    {
        "Numero": 1,
        "Nome": "Bulbasaur",
        "TipoPrimario": "Grama",
        "TipoSecundario": "Veneno",
        "Imagem": "001.png"
    },

    {
        "Numero": 2,
        "Nome": "Ivysaur",
        "TipoPrimario": "Grama",
        "TipoSecundario": "Veneno",
        "Imagem": "002.png"
    },

    {
        "Numero": 3,
        "Nome": "Venusaur",
        "TipoPrimario": "Grama",
        "TipoSecundario": "Veneno",
        "Imagem": "003.png"
    },

    {
        "Numero": 4,
        "Nome": "Charmander",
        "TipoPrimario": "Fogo",
        "TipoSecundario": "Nenhum",
        "Imagem": "004.png"
    },

    {
        "Numero": 5,
        "Nome": "Charmeleon",
        "TipoPrimario": "Fogo",
        "TipoSecundario": "Nenhum",
        "Imagem": "005.png"
    },

    {
        "Numero": 6,
        "Nome": "Charizard",
        "TipoPrimario": "Fogo",
        "TipoSecundario": "Voador",
        "Imagem": "006.png"
    },

    {
        "Numero": 7,
        "Nome": "Squirtle",
        "TipoPrimario": "Água",
        "TipoSecundario": "Nenhum",
        "Imagem": "007.png"
    },

    {
        "Numero": 8,
        "Nome": "Wartortle",
        "TipoPrimario": "Água",
        "TipoSecundario": "Nenhum",
        "Imagem": "008.png"
    },

    {
        "Numero": 9,
        "Nome": "Blastoise",
        "TipoPrimario": "Água",
        "TipoSecundario": "Nenhum",
        "Imagem": "009.png"
    },

    {
        "Numero": 10,
        "Nome": "Caterpie",
        "TipoPrimario": "Inseto",
        "TipoSecundario": "Nenhum",
        "Imagem": "010.png"
    }

])

print("# POKEDEX ATUALIZADA!!")

colecao.create_index("Numero", unique=True)

# contar documentos
print("Quantidade:", colecao.count_documents({}))

# mostrar nomes
for item in colecao.find().sort("Numero", 1):
    print(item["Numero"], "-", item["Nome"])

conn.close()