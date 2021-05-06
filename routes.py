from mysql.connector import  connection, Error
from flask import Flask, request
from comandos_bd import insert, select, update, delete


app = Flask(__name__)

# class Genero:
#     def __init__(self, nome, id=None):
#         self.nome = nome
#         self.id = id
#
#     def is_valid(self):
#         if len(self.nome) < 0:
#             return False
#
# def genero_from_web(nome):
#     return Genero(nome)
#
# def genero_from_db(nome, id):
#     return Genero(nome, id)
#
# def inserir_generos():
#     genero = genero_from_db(request.json["nome"] if "nome" in request.json)
#     if genero.is_valid():
#         inserir_generos(genero)
#         genero_salvo = get_genero(genero.nome)
#         genero_formatado = genero_from_db(genero_salvo)
#         return jsonify(genero_salvo.json())


@app.route("/generos", methods=["POST"])
def inserir_generos():
    pass

    # 1 - validar os parametros de entra
    # fazer um monte de if para checar se o que está sendo passado
    # é o que queremos
    # receber os dados de entrada em:
    # request.json["campo"]

    # 2 - converter o que vem da internet para uma estrutura interna
    # ex: criar um dict com os campos que precisamos
    # {"sigla": request.json["sigla"]}
    # isso é o serializer >> formtação

    # 3 - executar o que a função deveria fazer, no caso atual inserir estados
    # essa ação fica dentro do models

    # 4 - consultar a informação que queremos retornar >> fazer o select do item

    # 5 - Formatar os dados para retornar para o usuário com um serializer

    # 6 - retorna os dados formatados usando o jsonify