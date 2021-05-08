from flask import Flask, jsonify, request
from comandos_bd import query, execute
from models import *
from serializers import *
from validacao import valida_diretor, valida_id


app = Flask(__name__)

# criar enviar dados com json e retornar como json


@app.route("/diretores", methods=["POST"])
def inserir_diretor():
    diretor = diretores_from_web(**request.json)
    if valida_diretor(**diretor):
        id = insert_diretores(**diretor)
        diretor_inserido = get_diretores(id)
        return jsonify(diretores_from_db(diretor_inserido))
    else:
        return jsonify({"Erro": "Diretor inválido"})

# alterar diretor gênero filme usuário

@app.route("/diretores/<int:id>", methods=["PUT"])
def alterar_diretor(id):
    diretor = diretores_from_web(**request.json)
    if valida_diretor(**diretor):
        update_diretor(id, **diretor)
        #       diretor_alterado = get_diretores(id)
        return jsonify(diretores_from_db(update_diretor))
    else:
        return jsonify({"Erro": "Diretor inválido"})

# apagar diretor gênero filme usuário
# exibir mensagem de erro  ############### # set foreign_key_checks=0;
@app.route("/diretores/<int:id>", methods=["DELETE"])
def apagar_diretor(id):
    diretor_id = delete_id_from_web(**request.json)
    try:
        if valida_id(**diretor_id):
            delete_diretor(**diretor_id)
            return None, 204
    except:
        return jsonify({"Erro": "Diretor inexistente"})


@app.route("/diretores", methods=["GET"])
def buscar_diretor():
    diretor = diretores_from_web(**request.json)
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

@app.route("/usuarios", method=["GET"])
def select_usuario():
    nome_completo = nome_usuario_from_web(**request.args)
    usuarios = select_usuario(nome_completo)
    usuario_from_db = [usuario_from_db(usuarios) for usuario in usuarios]

# generos

@app.route("/generos", methods=["GET"])
def get_genero():
    genero = generos_from_web(**request.args)
    genero = get_genero(nome)
    generos_from_bd = generos_from_db for nome in generos
    return jsonify(generos_from_db)


@app.route("/generos", methods=["POST"])
def insert_genero():
    genero = generos_from_web(**request.json)
    if valida_genero(**genero):
        id_genero = insert_genero(**genero)
        genero_inserido = get_genero(id)
        return jsonify(genero_from_db(genero_inserido))
    else:
        return jsonify({"Erro": "Gênero inválido"})

@app.route("/generos/<int:id>", methods=["PUT"])
def udate_generos(id):
    genero = generos_from_web(**request.json)
    if valida_genero(**genero):
        update_genero(id, **genero)
        genero_inserido = get_genero(id)
        return jsonify(generos_from_db(genero_inserido))
    else:
        return jsonify({"Erro": "Gênero inválido"})

@app.route("/generos/<int:id>", methods=["DELETE"])
def delete_genero(id):
    try:
        delete_genero(id)
        return None, 204
    except:
        return jsonify({"Erro": "Gênero não encontrado"})









if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)