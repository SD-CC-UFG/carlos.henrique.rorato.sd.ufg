# Sistemas Distribuídos
# Aluno: Carlos Henrique Rorato Souza
# Lista 1 implementada com RPC - XML - Exercício 2 Servidor
# O cliente é análogo ao do exercício 1 - basta modificar as entradas.

from .xmlrpc.server import *

def maioridade(nome, sexo, idade):
    if sexo == "masculino":
        if idade >= 18: return True
    elif sexo == "feminino":
        if idade >= 21: return True
    else: return False

class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)

HOST = "localhost"
PORT = 5000

with SimpleXMLRPCServer((HOST, PORT), RequestHandler) as server:
    server.register_introspection_functions()
    server.register_function(maioridade)
    server.serve_forever()
