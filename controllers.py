from flask import Flask, jsonify, request
from comandos_bd import *
from models import *
from serializers import *
from validacao import *
app = Flask(__name__)


@app.route("/diretores", methods=["POST"])
def inserir_diretor():
    diretor = diretores_from_web(**request.json)
    if valida_diretor(**diretor):
        id = insert_diretores(**diretor)
        diretor_inserido = get_diretores(id)
        return jsonify(diretores_from_db(diretor_inserido))
    else:
        return jsonify({"Erro": "Diretor inválido"})


@app.route("/diretores/<int:id>", methods=["PUT"])
def alterar_diretor(id):
    diretor = diretores_from_web(**request.json)
    if valida_diretor(**diretor):
        update_diretor(id, **diretor)
        diretor_alterado = get_diretores(id)
        return jsonify(diretores_from_db(diretor_alterado))
    else:
        return jsonify({"Erro": "Diretor inválido"})


@app.route("/diretores/<int:id>", methods=["DELETE"])
def apagar_diretor(id):
    diretor_id = delete_diretor(**request.json)
    try:
        if valida_id(**diretor_id):
            delete_diretor(**diretor_id)
            return None, 204
    except:
        return jsonify({"Erro": "Diretor inexistente"})


@app.route("/diretores", methods=["GET"])
def buscar_diretor():
    diretor = diretores_from_web(**request.args)
    diretores_selecionado = select_diretor(**diretor)
    if len(diretores_selecionado) > 0:
        return jsonify(diretores_from_db(**diretores_selecionado))
    else:
        return jsonify({"Erro": "Não foi possível achar este diretor"})

 #  usuario

@app.route("/usuarios", method=["POST"])  # 1 Checa a rota
def inserir_usuario():
    usuario = usuario_from_web(**request.json)
    if valida_usuario(**usuario):
        id_usuario = insert_usuario(**usuario)
        usuario_cadastrado = get_usuario(id_usuario)
        return jsonify(usuario_from_db(usuario_cadastrado))
    else:
        return jsonify({"Erro": "Usuário inválido"})

@app.route("/users/<int:id>", methods=["PUT", "PATCH"])
def update_users(id):
    user = serializers.users_from_web(**request.json)
    if valida_usuario(**user):
        models.update_user(id, **user)
        inserted_user = models.get_user(id)
        return jsonify(serializers.users_from_db(inserted_user))
    else:
        return jsonify({"erro": "Usuário inválido"})

@app.route("/usuarios", method=["GET"])
def select_usuario():
    nome_completo = usuario_from_web(**request.args)
    usuarios = select_usuario(nome_completo)
    usuario_from_db = [usuario_from_db(usuarios) for usuario in usuarios]
    return jsonify(usuario_from_db)


@app.route("/generos", methods=["GET"])
def get_genero():
    genero = generos_from_web(**request.args)
    generos_from_bd = [serializers.generos_from_db for nome in generos]
    return jsonify(generos_from_db)


@app.route("/generos", methods=["POST"])
def insert_genero():
    genero = generos_from_web(**request.json)
    if valida_genero(**genero):
        id_genero = insert_genero(**genero)
        genero_inserido = get_genero(id)
        return jsonify(generos_from_db(genero_inserido))
    else:
        return jsonify({"Erro": "Gênero inválido"})

@app.route("/generos/<int:id>", methods=["PUT"])
def update_generos(id):
    genero = generos_from_web(**request.json)
    if valida_genero(**genero):
        update_genero(id, **genero)
        genero_alterado = get_genero(id)
        return jsonify(generos_from_db(genero_alterado))
    else:
        return jsonify({"Erro": "Gênero inválido"})

@app.route("/generos/<int:id>", methods=["DELETE"])
def delete_genero(id):
    try:
        delete_genero(id)
        return "", 204
    except:
        return jsonify({"Erro": "Gênero não encontrado"})



if __name__ == "__main__":
    app.run(host='127.0.0.1', debug=True)