# Sistemas Distribuídos
# Aluno: Carlos Henrique Rorato Souza
# Lista 1 implementada com RPC - XML - Exercício 4 Servidor
# O cliente é análogo ao do exercício 1 - basta modificar as entradas.

from xmlrpc.server import *

def pIdeal(altura, sexo):
    if sexo == "masculino":
        return (72.7 * altura) - 58
    else:
        return (62.1 * altura) - 44.7

class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)

HOST = "localhost"
PORT = 5000

with SimpleXMLRPCServer((HOST, PORT), RequestHandler) as server:
    server.register_introspection_functions()
    server.register_function(pIdeal)
    server.serve_forever()
