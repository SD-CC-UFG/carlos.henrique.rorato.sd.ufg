# Sistemas Distribuídos
# Aluno: Carlos Henrique Rorato Souza
# Lista 1 implementada com CORBA - Exercício 1 Cliente
# Este cliente pode ser utilizado para todos os exercícios,
# basta que sejam modificadas as entradas e chamadas de função

import CORBA, Exercicio

orb = CORBA.ORB_init()

o = orb.string_to_object("corbaloc::host.example.com/Exercicio")

o = o._narrow(Exercicio.ServidorExercicio)

n = input("Informe seu nome:")
cg = input("Informe o cargo ocupado (programador, operador): ") 
sal = float(input("Informe o seu salário: "))

print o.calcula_sal(n, cg, sal)