# Sistemas Distribuídos
# Aluno: Carlos Henrique Rorato Souza
# Lista 1 implementada com RPC - XML - Exercício 1 Servidor

from .xmlrpc.server import *

def calcula_sal(n, cg, sal):   
    if cg == "operador":
        sal *= 1.2
    elif cg == "programador":
        sal *= 1.18
    return "Nome do funcionario:" + n + " sal reajustado" + sal

class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)


HOST = "localhost"
PORT = 5000

with SimpleXMLRPCServer((HOST, PORT), RequestHandler) as server:
    server.register_introspection_functions()
    server.register_function(calcula_sal)
    server.serve_forever()
