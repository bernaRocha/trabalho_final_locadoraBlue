from comandos_bd import insert, select_like, update, delete, select

# return em todos os INSERTS
# gênero filme usuário

# def para diretores

def insert_diretores(nome_completo):
    return insert("diretores", ["nome_completo"], [nome_completo])

def get_diretores(id):
    return select("diretores", "id", id)

def update_diretor(id, nome_completo):
    return update("diretores", "id", id, "nome_completo", [nome_completo])

def delete_diretor(id):
    return delete("diretores", "id", id)

def select_diretor(nome_completo):
    return select_like("diretores", "nome_completo", f"%{nome_completo}%")


 # def para genero

def insert_genero(id, nome):
    return insert("genero", ["id", "nome"], [id, nome])

def get_genero(id):
    return select("generos", "id", id)

def update_genero(id, nome):
    update("generos", "id", id, "nome", [nome])

def delete_genero(id):
    delete("generos", "id", id)

def select_generos(id, nome):
    return select("generos", "nome", f"%{nome}%")

######  def para usuario

def insert_usuario(nome_completo, CPF):
    return insert("usuarios", ["nome_completo", "CPF"], [nome_completo, CPF])

def get_usuario(id_usuario):
    return select("usuarios", "id", id_usuario)[0]

def update_usuario(id_usuario, nome_completo, CPF):
    update("usuarios", "id", id_usuario, ["nome_completo", "CPF"],[nome_completo, CPF])

def delete_usuario(id):
    return delete("usuarios", "id", id)

def select_usuario(id, nome_completo):
    return select_like("usuarios", "nome_completo", f"%{nome_completo}%")

#### def para filmes

def insert_filme(titulo, ano, classificacao, preco, diretores_id, generos_id):
    insert("genero", ["titulo", "ano", "classificacao", "preco", "diretores_id", "generos_id"],
           [titulo, ano, classificacao, preco, diretores_id, generos_id])


def select_filme(titulo, ano, classificacao, preco, diretores_id, generos_id):
    select("filmes", ['titulo', 'ano', 'classificacao', 'preco', 'diretores_id', 'generos_id'],
           f"%{titulo, ano, classificacao, preco, diretores_id, generos_id}%")
    return titulo, ano, classificacao, preco, diretores_id, generos_id


def get_filme(id):
    return select("filmes", "id", id)[0]

def update_filme(id, titulo, ano, classificacao, preco, diretores_id, generos_id):
    update("filmes", "id", id, ["titulo", "ano", "classificacao", "preco", "diretores_id", "generos_id"],
           [titulo, ano, classificacao, preco, diretores_id, generos_id])


def delete_filme(id):
    delete("filmes", "id", id)

# def update