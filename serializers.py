def diretores_from_web(**kwargs):
    return {
        "nome_completo": kwargs["nome_completo"] if "nome_completo" in kwargs else ""
    }

def diretores_from_db(*args):
    return[{
        "nome_completo": diretor[0][1]
    } for diretor in args]

def usuario_from_web(**kwargs):
    return {
        "nome_completo": kwargs["nome_completo"] if "nome_completo" in kwargs else "",
        "CPF": kwargs["CPF"] if "CPF" in kwargs else "",
    }

def usuario_from_db(usuarios):
    return {
        "id": usuarios["id"],
        "nome_completo": usuarios["nome_completo"],
        "CPF": usuarios["CPF"]
    }


def filmes_from_web(**kwargs):
    return{
        "titulo": kwargs["titulo"] if "titulo" in kwargs else "",
        "ano": kwargs["ano"] if "ano" in kwargs else "",
        "classificacao": kwargs["classificacao"] if "classificacao" in kwargs else "",
        "preco": kwargs["preco"] if "preco" in kwargs else "",
        "diretores_id": kwargs["diretores_id"] if "diretores_id" in kwargs else "",
        "generos_id": kwargs["generos_id"] if "generos_id" in kwargs else ""
    }


def filmes_from_db(filmes):
    return{
        "titulo": filmes["titulo"],
        "ano": filmes["ano"],
        "classificacao": filmes["classificacao"],
        "preco": filmes["preco"],
        "diretores_id": filmes["diretores_id"],
        "generos_id": filmes["generos_id"]
    }


def generos_from_web(**kwargs):
    return{
        "nome": kwargs["nome"] if "nome" in kwargs else "",
    }

def generos_from_db(generos):
    return{
        "nome_completo": generos["nome_completo"],
    }