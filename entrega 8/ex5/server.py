# Sistemas Distribuídos
# Aluno: Carlos Henrique Rorato Souza
# Lista 1 implementada com CORBA - Exercício 5 Servidor
# O cliente é análogo ao do exercício 1 - basta modificar as entradas.

import sys, os
import CORBA, Exercicio, Exercicio__POA

EXERCICIO_PATH = "./"

class CookieServer_i (Exercicio__POA.ServidorExercicio):
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

orb = CORBA.ORB_init(sys.argv)
poa = orb.resolve_initial_references("RootPOA")

servant = CookieServer_i()
poa.activate_object(servant)

print orb.object_to_string(servant._this())

poa._get_the_POAManager().activate()
orb.run()