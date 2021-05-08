from models import insert_diretores, get_diretores, update_diretor, delete_diretor, select_diretor


def valida_diretor(nome_completo):
    if len(nome_completo) == 0:
        return False

    return True


def valida_id(id):
    if id == 0:
        return False
    else:
        return True

def valida_usuario(nome_completo, CPF):
    if len(nome_completo) == 0:
        return False
    if len(CPF) != 14:
        return False
    return True