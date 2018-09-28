# Sistemas Distribuídos
# Aluno: Carlos Henrique Rorato Souza
# Lista 1 implementada com RPC - XML - Exercício 3 Servidor
# O cliente é análogo ao do exercício 1 - basta modificar as entradas.

from xmlrpc.server import *

def ap(notas):
    if (notas[0] + notas[1])/2 >= 7.0:
        return "O aluno está aprovado por média!"
    elif (notas[0] + notas[1])/2 >= 3.0:
        return "O aluno precisa fazer a prova N3"
    else:
        return "O aluno está reprovado por média!"


class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)

HOST = "localhost"
PORT = 5000

with SimpleXMLRPCServer((HOST, PORT), RequestHandler) as server:
    server.register_introspection_functions()
    server.register_function(ap)
    server.serve_forever()