# Sistemas Distribuídos
# Aluno: Carlos Henrique Rorato Souza
# Lista 1 implementada com CORBA - Exercício 1 Servidor

import sys, os
import CORBA, Exercicio, Exercicio__POA

EXERCICIO_PATH = "./"

class CookieServer_i (Exercicio__POA.ServidorExercicio):
    def calcula_sal(n, cg, sal):   
	    if cg == "operador":
	        sal *= 1.2
	    elif cg == "programador":
	        sal *= 1.18
	    return "Nome do funcionario:" + n + " sal reajustado" + sal

orb = CORBA.ORB_init(sys.argv)
poa = orb.resolve_initial_references("RootPOA")

servant = CookieServer_i()
poa.activate_object(servant)

print orb.object_to_string(servant._this())

poa._get_the_POAManager().activate()
orb.run()