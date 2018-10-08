# Sistemas Distribuídos
# Aluno: Carlos Henrique Rorato Souza
# Lista 1 implementada com RMI - Exercício 2 Servidor
# O cliente é análogo ao do exercício 1 - basta modificar as entradas.

import Pyro4

@Pyro4.expose
class Problema:
	def maioridade(nome, sexo, idade):
	    if sexo == "masculino":
	        if idade >= 18: return True
	    elif sexo == "feminino":
	        if idade >= 21: return True
	    else: return False

daemon = Pyro4.Daemon()

uri = daemon.register(Problema)
ns = Pyro4.locateNS()
ns.register('obj', uri)
print(uri)

daemon.requestLoop()

