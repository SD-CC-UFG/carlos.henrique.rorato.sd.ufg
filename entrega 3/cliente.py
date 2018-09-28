# Sistemas Distribuídos
# Aluno: Carlos Henrique Rorato Souza e Juliana de Melo
# Chat Simples com Thread Pool

from threading import Thread
import socket
import os
import sys
import select

#Conectando-se com o servidor, através dos argumentos da linha de comando
cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
IP = str(sys.argv[1])
PORT = int(sys.argv[2])
cliente.connect((IP , PORT))

#Função que faz a leitura da mensagem e a envia ao servidor
# utilizando o socket
def fazer_envio():
	while True:
		mensagem =  sys.stdin.readline()
		cliente.send(mensagem)
		print(mensagem)

#Função para receber o resultado
def receber_resultado():
	while True:
		mensagem = cliente.recv(1024)
		print mensagem

#Inicializando as threads para se conectar ao servidor
td1 = Thread(target=fazer_envio)
td2 = Thread(target=receber_resultado)
td1.start()
td2.start()
