def diretores_from_web(**kwargs):
    return {
        "nome_completo": kwargs["nome_completo"] if "nome_completo" in kwargs else ""
    }

def diretores_from_db(**args):
    return[{
        "nome_completo": diretor[0][1]
    } for diretor in args]

def delete_id_from_web(**kwargs):
    return {
        "id": kwargs["id"] if "id" in kwargs else " "
    }