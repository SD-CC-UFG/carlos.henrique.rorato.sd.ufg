# Sistemas Distribuídos
# Aluno: Carlos Henrique Rorato Souza
# Lista 1 implementada com RPC - XML - Exercício 1 Cliente
# Este cliente pode ser utilizado para todos os exercícios,
# basta que sejam modificadas as entradas (inputs)

import xmlrpc.client

s = xmlrpc.client.ServerProxy('http://localhost:5000')

n = input("Informe seu nome:")
cg = input("Informe o cargo ocupado (programador, operador): ") 
sal = float(input("Informe o seu salário: "))

print(s.atualiza_salario(n, cg, sal))
