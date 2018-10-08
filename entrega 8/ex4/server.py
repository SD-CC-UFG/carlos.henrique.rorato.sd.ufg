# Sistemas Distribuídos
# Aluno: Carlos Henrique Rorato Souza
# Lista 1 implementada com CORBA - Exercício 4 Servidor
# O cliente é análogo ao do exercício 1 - basta modificar as entradas.

import sys, os
import CORBA, Exercicio, Exercicio__POA

EXERCICIO_PATH = "./"

class CookieServer_i (Exercicio__POA.ServidorExercicio):
    def pIdeal(altura, sexo):
	    if sexo == "masculino":
	        return (72.7 * altura) - 58
	    else:
	        return (62.1 * altura) - 44.7

orb = CORBA.ORB_init(sys.argv)
poa = orb.resolve_initial_references("RootPOA")

servant = CookieServer_i()
poa.activate_object(servant)

print orb.object_to_string(servant._this())

poa._get_the_POAManager().activate()
orb.run()