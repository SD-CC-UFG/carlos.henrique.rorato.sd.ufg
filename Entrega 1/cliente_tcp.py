# Sistemas Distribuídos
# Aluno: Carlos Henrique Rorato Souza
# Mandando mensagem para um servidor utilizando TCP
# Módulo Cliente

import socket
HOST = '127.0.0.1' # IP do Servidor
PORT = 5000        # Porta do Servidor

# Abrindo a conexão:
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
dest = (HOST, PORT)
tcp.connect(dest)

print('Escreva uma mensagem. Para sair use CTRL+X\n')
msg = input()

while msg != '\x18':
    tcp.send(msg.encode('utf-8'))
    resposta = tcp.recv(1024)
    print(resposta)
    msg = input()

tcp.close() # Fechando a Conexão