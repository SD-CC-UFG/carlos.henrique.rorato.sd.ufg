# Sistemas Distribuídos
# Aluno: Carlos Henrique Rorato Souza
# Mandando mensagem para um servidor utilizando TCP
# Módulo Servidor

import socket
HOST = '' # IP do Servidor
PORT = 5000        # Porta do Servidor

# Abrindo a conexão:
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Criar o socket
orig = (HOST, PORT)

tcp.bind(orig) # Coloca um endereço local, endereço IP e porta no socket
tcp.listen(1) # Coloca o socket em modo "passivo", aguardando

while True:
    con, cliente = tcp.accept()
    print('Concetado por', cliente)
    while True:
        msg = con.recv(1024)
        if not msg: break
        print(cliente, msg)
        recebido = "Resposta recebida no servidor com sucesso!"
        con.send(recebido.encode('utf-8'))
    print('Finalizando conexao do cliente', cliente)
    con.close()