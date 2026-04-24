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
        "Imagem": "001.png",
        "Altura": "0.7 m",
        "Peso": "6.9 kg",
        "Descricao": "Uma semente estranha foi plantada em suas costas no nascimento. A planta brota e cresce com este Pokémon."
    },
    {
        "Numero": 2,
        "Nome": "Ivysaur",
        "TipoPrimario": "Grama",
        "TipoSecundario": "Veneno",
        "Imagem": "002.png",
        "Altura": "1.0 m",
        "Peso": "13.0 kg",
        "Descricao": "Quando o bulbo em suas costas cresce, parece perder a capacidade de ficar de pé em suas patas traseiras."
    },
    {
        "Numero": 3,
        "Nome": "Venusaur",
        "TipoPrimario": "Grama",
        "TipoSecundario": "Veneno",
        "Imagem": "003.png",
        "Altura": "2.0 m",
        "Peso": "100.0 kg",
        "Descricao": "A planta floresce absorvendo energia solar. Ela permanece em movimento para buscar a luz do sol."
    },
    {
        "Numero": 4,
        "Nome": "Charmander",
        "TipoPrimario": "Fogo",
        "TipoSecundario": "Nenhum",
        "Imagem": "004.png",
        "Altura": "0.6 m",
        "Peso": "8.5 kg",
        "Descricao": "Prefere lugares quentes. Quando chove, dizem que o vapor jorra da ponta de sua cauda."
    },
    {
        "Numero": 5,
        "Nome": "Charmeleon",
        "TipoPrimario": "Fogo",
        "TipoSecundario": "Nenhum",
        "Imagem": "005.png",
        "Altura": "1.1 m",
        "Peso": "19.0 kg",
        "Descricao": "Quando balança sua cauda em chamas, ele eleva a temperatura ao seu redor a níveis insuportáveis."
    },
    {
        "Numero": 6,
        "Nome": "Charizard",
        "TipoPrimario": "Fogo",
        "TipoSecundario": "Voador",
        "Imagem": "006.png",
        "Altura": "1.7 m",
        "Peso": "90.5 kg",
        "Descricao": "Cospe fogo que é quente o suficiente para derreter rochas. Pode causar incêndios florestais soprando chamas."
    },
    {
        "Numero": 7,
        "Nome": "Squirtle",
        "TipoPrimario": "Água",
        "TipoSecundario": "Nenhum",
        "Imagem": "007.png",
        "Altura": "0.5 m",
        "Peso": "9.0 kg",
        "Descricao": "Após o nascimento, suas costas incham e endurecem formando um casco. Ele borrifa espuma poderosa pela boca."
    },
    {
        "Numero": 8,
        "Nome": "Wartortle",
        "TipoPrimario": "Água",
        "TipoSecundario": "Nenhum",
        "Imagem": "008.png",
        "Altura": "1.0 m",
        "Peso": "22.5 kg",
        "Descricao": "Muitas vezes se esconde na água para vigiar presas incautas. Ao nadar rapidamente, move suas orelhas para manter o equilíbrio."
    },
    {
        "Numero": 9,
        "Nome": "Blastoise",
        "TipoPrimario": "Água",
        "TipoSecundario": "Nenhum",
        "Imagem": "009.png",
        "Altura": "1.6 m",
        "Peso": "85.5 kg",
        "Descricao": "Um Pokémon brutal com jatos de água pressurizada em seu casco. Eles são usados para ataques de alta velocidade."
    },
    {
        "Numero": 10,
        "Nome": "Caterpie",
        "TipoPrimario": "Inseto",
        "TipoSecundario": "Nenhum",
        "Imagem": "010.png",
        "Altura": "0.3 m",
        "Peso": "2.9 kg",
        "Descricao": "Suas pernas curtas são cobertas com ventosas que lhe permitem escalar paredes e árvores incansavelmente."
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