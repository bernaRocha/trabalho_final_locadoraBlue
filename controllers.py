from flask import Flask, jsonify, request
from models import insert_diretores, get_diretores, update_diretor, delete_diretor, select_diretor
from serializers import diretores_from_web, diretores_from_db, delete_id_from_web
from validacao import valida_diretor, valida_id


app = Flask(__name__)

# criar: diretor, gênero, filme e usuário
# criar enviar dados com json e retornar como json


@app.route("/diretores", method=["POST"])
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
        return (None, 201)  ################ ver em aula
    else:
        return jsonify({"Erro": "Diretor inválido"})


# apagar diretor gênero filme usuário
# exibir mensagem de erro  ############### # set foreign_key_checks=0;
@app.route("diretores/<int:id>", methods=["DELETE"])
def apagar_diretor(id):
    diretor_id = delete_id_from_web(**request.json)
    try:
        if valida_id(**diretor_id):
            delete_diretor(**diretor_id)
            return(None,204)
    except:
        return jsonify({"Erro": "Diretor inexistente"})


# buscar
@app.route("/diretores", methods=["GET"])
def buscar_diretor():
    diretor = diretores_from_web(**request.json)
    diretores_selecionado = select_diretor(**diretor)
    if len(diretores_selecionado) > 0:
        return jsonify(diretores_from_db(**diretores_selecionado))
    else:
        return jsonify({"Erro": "Não foi possível achar este diretor"})


