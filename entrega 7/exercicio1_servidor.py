# Sistemas Distribuídos
# Aluno: Carlos Henrique Rorato Souza
# Lista 1 implementada com RMI - Exercício 1 Servidor

import Pyro4

@Pyro4.expose
class Problema:
	def calcula_sal(n, cg, sal):   
	    if cg == "operador":
	        sal *= 1.2
	    elif cg == "programador":
	        sal *= 1.18
	    return "Nome do funcionario:" + n + " sal reajustado" + sal

daemon = Pyro4.Daemon()

uri = daemon.register(Problema)
ns = Pyro4.locateNS()
ns.register('obj', uri)
print(uri)

daemon.requestLoop()
