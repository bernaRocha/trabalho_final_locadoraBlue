from flask import Flask, jsonify, request
from comandos_bd import query, execute, insert, update, select, delete
from decimal import Decimal

# diretor gênro filme usuário
# insert/ post select/ get delete/ delete  update/ put/patch
app = Flask(__name__)

@app.route("/diretores", methods=["GET", "PUT", "DELETE", "POST"])
def diretores():
    if request.method == "GET":
        return jsonify(select("diretores"))
    elif request.method == "PUT":
        return jsonify(update("diretores", "nome_completo", (request.json["nome"],))) #vírgula pq é tupla de um item apenas
    elif request.method == "POST":
        return jsonify(insert("diretores", "nome_completo", request.json["id"]))
    elif request.method == "DELETE":
        return jsonify(delete("diretores", "id", request.json["id"]))

@app.route("/genero", methods=["GET", "PUT", "DELETE", "POST"])
def genero():
    if request.method == "GET":
        return jsonify(select("genero"))
    elif request.method == "PUT":
        return jsonify(update("id", "nome_completo", (request.json["nome"],)))  # dúvida aqui
    elif request.method == "POST":
        return jsonify(insert("id", "nome", request.json["nome"]))
    elif request.method == "DELETE":
        return jsonify(delete("id", "nome", request.json["id"]))


@app.route("/filme",methods=["GET", "POST", "DELETE", "PUT"])
def filme(titulo, ano, classificacao, preco, diretores_id, generos_id):
    if request.method == "GET":
        return jsonify(select("filmes"))
    elif request.method == "POST":
        return jsonify(insert('filmes',["titulo", "ano", "classificacao", "preco", "diretores_id", "generos_id"],
        [titulo, ano, classificacao, preco, diretores_id, generos_id]),(request.json["id",]))
    elif request.method == "DELETE":
        return jsonify(delete("titulo"),(request.json["id",]))    # dúvida aqui
    elif request.method == "PUT":
        return jsonify(update("titulo", "ano", "classificacao", "preco", "diretores_id"),
                       (request.json["titulo"],))


@app.route("/usuarios", methods=["GET", "PUT", "DELETE", "POST"])
def usuarios():
    if request.method == "GET":
        return jsonify(select("usuarios"))
    elif request.method == "PUT":
        return jsonify(update('usuarios', 'id', id, ["id", "nome_completo", "CPF"], (request.json["nome_completo", "CPF"]),))
    elif request.method == "POST":
        return jsonify(insert("id", "nome_completo", "CPF", request.json["nome_completo"]))  # tirar dúvida sobre isso
    elif request.method == "DELETE":
        return jsonify(delete("nome_completo", "CPF", request.json["nome_completo"]))


