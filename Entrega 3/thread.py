# Sistemas Distribuídos
# Aluno: Carlos Henrique Rorato Souza
# Mandando mensagem para um servidor utilizando TCP - Múltiplas conexões TCP
# Módulo Thread  - Threads Distribuídas

import threading
import socket

HOST = '' # IP do Servidor
PORT = 5001        # Porta do Servidor

def conexaoTCP(con, cliente):
	print('Concetado por', cliente)
	while True:
		msg = con.recv(1024)
		if not msg: break
		print(cliente, msg)
		recebido = "Resposta recebida no servidor com sucesso!"
		con.send(recebido.encode('utf-8'))
	print('Finalizando conexao do cliente', cliente)
	con.close()

# Abrindo a conexão com o cliente:
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Criar o socket
orig = (HOST, PORT)

tcp.bind(orig) # Coloca um endereço local, endereço IP e porta no socket
tcp.listen(1) # Coloca o socket em modo "passivo", aguardando

while True:
    con, cliente = tcp.accept()
    t = threading.Thread(target=conexaoTCP,args=(con, cliente))
    t.start()