# Sistemas Distribuídos
# Aluno: Carlos Henrique Rorato Souza
# Lista 1 implementada com RMI - Exercício 3 Servidor
# O cliente é análogo ao do exercício 1 - basta modificar as entradas.

import Pyro4

@Pyro4.expose
class Problema:
    def ap(notas):
        if (notas[0] + notas[1])/2 >= 7.0:
            return "O aluno está aprovado por média!"
        elif (notas[0] + notas[1])/2 >= 3.0:
            return "O aluno precisa fazer a prova N3"
        else:
            return "O aluno está reprovado por média!"

daemon = Pyro4.Daemon()

uri = daemon.register(Problema)
ns = Pyro4.locateNS()
ns.register('obj', uri)
print(uri)

daemon.requestLoop()






