# Sistemas Distribuídos
# Aluno: Carlos Henrique Rorato Souza
# Lista 1 implementada com RMI - Exercício 4 Servidor
# O cliente é análogo ao do exercício 1 - basta modificar as entradas.

import Pyro4

@Pyro4.expose
class Problema:
	def pIdeal(altura, sexo):
	    if sexo == "masculino":
	        return (72.7 * altura) - 58
	    else:
	        return (62.1 * altura) - 44.7

daemon = Pyro4.Daemon()

uri = daemon.register(Problema)
ns = Pyro4.locateNS()
ns.register('obj', uri)
print(uri)

daemon.requestLoop()


