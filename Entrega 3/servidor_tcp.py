# Sistemas Distribuídos
# Aluno: Carlos Henrique Rorato Souza
# Mandando mensagem para um servidor utilizando TCP - Múltiplas conexões TCP
# Módulo Servidor - Threads Distribuídas

import time
import socket

HOST = '' # IP do Servidor
PORT = 5000        # Porta do Servidor

def MandaThread(con, cliente):
	print('Concetado por', cliente)
	while True:
		msg = con.recv(1024)
		if not msg: break
		print(cliente, msg)
		print("Encaminhando para a thread...")

		thread.send(msg) # Manda a mensagem para a Thread distribuída processar
		confirm = thread.recv(1024)

		con.send(confirm)
		
	print('Finalizando conexao do cliente', cliente)
	con.close()

#abrindo a conexão com as threads:
thread = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
dest = ('127.0.0.1', 5001)
thread.connect(dest)


# Abrindo a conexão com o cliente:
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Criar o socket
orig = (HOST, PORT)

tcp.bind(orig) # Coloca um endereço local, endereço IP e porta no socket
tcp.listen(1) # Coloca o socket em modo "passivo", aguardando

while True:
	con, cliente = tcp.accept()
	MandaThread(con, cliente)


