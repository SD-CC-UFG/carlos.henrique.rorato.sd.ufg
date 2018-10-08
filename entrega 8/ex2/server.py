# Sistemas Distribuídos
# Aluno: Carlos Henrique Rorato Souza
# Lista 1 implementada com CORBA - Exercício 2 Servidor
# O cliente é análogo ao do exercício 1 - basta modificar as entradas.

import sys, os
import CORBA, Exercicio, Exercicio__POA

EXERCICIO_PATH = "./"

class CookieServer_i (Exercicio__POA.ServidorExercicio):
	def maioridade(nome, sexo, idade):
		    if sexo == "masculino":
		        if idade >= 18: return True
		    elif sexo == "feminino":
		        if idade >= 21: return True
		    else: return False

orb = CORBA.ORB_init(sys.argv)
poa = orb.resolve_initial_references("RootPOA")

servant = CookieServer_i()
poa.activate_object(servant)

print orb.object_to_string(servant._this())

poa._get_the_POAManager().activate()
orb.run()