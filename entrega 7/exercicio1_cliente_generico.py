# Sistemas Distribuídos
# Aluno: Carlos Henrique Rorato Souza
# Lista 1 implementada com RMI - Exercício 1 Cliente
# Este cliente pode ser utilizado para todos os exercícios,
# basta que sejam modificadas as entradas e chamadas de função

import  Pyro4

ns = Pyro4.locateNS()

uri = ns.lookup('obj')

o = Pyro4.Proxy(uri)

n = input("Informe seu nome:")
cg = input("Informe o cargo ocupado (programador, operador): ") 
sal = float(input("Informe o seu salário: "))

print(o.calcula_sal(n, cg, sal))

