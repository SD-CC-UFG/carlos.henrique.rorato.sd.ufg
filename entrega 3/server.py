# Sistemas Distribuídos
# Aluno: Carlos Henrique Rorato Souza e Juliana de Melo
# Chat Simples com Thread Pool

import sys
from threadPool import ThreadPool
import socket
import os

#Sockets para o servidor, com IP e porta definidos por linha de comando
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
IP = str(sys.argv[1])
PORT = int(sys.argv[2])
s.bind((IP , PORT))
#coloca o servidor em modo de "escuta", aguardando a conexão pelos clientes
s.listen(100)

clientes = [] #lista para os clientes

def novo_cliente(cnx, end):
	cnx.send("você está conectado ao chat.")
	while True:
		msg = cnx.recv(1024)
		if msg:
			print end[0] + ": " + msg
			msgEnvio = end[0] + ": " + msg
			envia_todos(msgEnvio, cnx)
		else:
			if cnx in clientes:
				clientes.remove(cnx)

def Principal():
	thread = ThreadPool(10)
	while True:
		cnx, end = s.accept()
		print "o seguinte endereço se conectou: " + end[0]
		clientes.append(cnx)
		thread.insert_job(novo_cliente, cnx, end)

def envia_todos(msg, cnx): #envia a msg para todos os clientes conectados.
	for k in clientes:
		if k != cnx:
			try:
				k.send(str(msg))
			except:
				k.close()
				if k in clientes:
					clientes.remove(k)


Principal()
cnx.close()
s.close()
