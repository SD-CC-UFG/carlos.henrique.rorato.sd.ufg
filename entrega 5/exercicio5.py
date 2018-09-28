# Sistemas Distribuídos
# Aluno: Carlos Henrique Rorato Souza
# Lista 1 implementada com RPC - XML - Exercício 5 Servidor
# O cliente é análogo ao do exercício 1 - basta modificar as entradas.

from xmlrpc.server import *

def classifica(idade):
    if idade < 5:
        return "Não pode participar"
    elif idade < 8:
        return "infantil A"
    elif idade < 11:
        return "infantil B"
    elif idade < 14:
        return "juvenil A"
    elif idade < 18:
        return "juvenil B"
    else:
        return "adulto"


class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)

HOST = "localhost"
PORT = 5000

with SimpleXMLRPCServer((HOST, PORT), RequestHandler) as server:
    server.register_introspection_functions()
    server.register_function(classifica)
    server.serve_forever()