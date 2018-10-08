# Sistemas Distribuídos
# Aluno: Carlos Henrique Rorato Souza
# Lista 1 implementada com RMI - Exercício 5 Servidor
# O cliente é análogo ao do exercício 1 - basta modificar as entradas.

import Pyro4

@Pyro4.expose
class Problema:
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

daemon = Pyro4.Daemon()

uri = daemon.register(Problema)
ns = Pyro4.locateNS()
ns.register('obj', uri)
print(uri)

daemon.requestLoop()