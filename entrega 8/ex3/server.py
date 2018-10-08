# Sistemas Distribuídos
# Aluno: Carlos Henrique Rorato Souza
# Lista 1 implementada com CORBA - Exercício 3 Servidor
# O cliente é análogo ao do exercício 1 - basta modificar as entradas.

import sys, os
import CORBA, Exercicio, Exercicio__POA

EXERCICIO_PATH = "./"

class CookieServer_i (Exercicio__POA.ServidorExercicio):
    def ap(notas):
        if (notas[0] + notas[1])/2 >= 7.0:
            return "O aluno está aprovado por média!"
        elif (notas[0] + notas[1])/2 >= 3.0:
            return "O aluno precisa fazer a prova N3"
        else:
            return "O aluno está reprovado por média!"

orb = CORBA.ORB_init(sys.argv)
poa = orb.resolve_initial_references("RootPOA")

servant = CookieServer_i()
poa.activate_object(servant)

print orb.object_to_string(servant._this())

poa._get_the_POAManager().activate()
orb.run()