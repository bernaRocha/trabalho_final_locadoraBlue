from comandos_bd import insert, select_like, update, delete


# diretor gênero filme usuário

# def insert

def insert_diretores(nome_completo):
    return insert("diretores", ["nome_completo"], [nome_completo])

def get_diretores(id):
    return select("diretores", "id", id)

def update_diretor(id, nome_completo):
    return update("diretores", "id", id, "nome_completo", [nome_completo])

def delete_diretor(id):
    return delete("diretores", "id", id)

def select_diretor(nome_completo):
    select_like("diretores", "nome_completo", f"%{nome_completo}%")


def insert_genero(id, nome):
    insert("genero", ["id", "nome"], [id, nome])


def insert_filme(titulo, ano, classificacao, preco, diretores_id, generos_id):
    insert("genero", ["titulo", "ano", "classificacao", "preco", "diretores_id", "generos_id"],
           [titulo, ano, classificacao, preco, diretores_id, generos_id])


def insert_usuario(nome_completo, CPF):
    insert("usuarios", ["nome_completo", "CPF"], [nome_completo, CPF])

#   def select

def select_diretor(id, nome_completo):
    select("diretores", ['id', 'nome_completo'], f"%{id, nome_completo}%")
    return id, nome_completo


def select_genero(id, nome):
    select("generos", ['id', 'nome'], f"%{id, nome}%")
    return id, nome

def select_filme(titulo, ano, classificacao, preco, diretores_id, generos_id):
    select("filmes", ['titulo', 'ano', 'classificacao', 'preco', 'diretores_id', 'generos_id'],
           f"%{titulo, ano, classificacao, preco, diretores_id, generos_id}%")
    return titulo, ano, classificacao, preco, diretores_id, generos_id

def select_usuario(id, nome_completo, cpf):
    select("usuarios", ['id', 'nome_completo', 'CPF'], f"%{id, nome_completo, cpf}%")
    return id, nome_completo, cpf
# def update


def update_genero():
    update()

def update_filme():
    update()

def update_usuario():
    update()
