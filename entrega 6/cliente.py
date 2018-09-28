# Sistemas Distribuídos
# Aluno: Carlos Henrique Rorato Souza
# Comunicação cliente/servidor com linguagens diferentes
# Módulo Cliente - Python
# Esta implementação utiliza sockets

import socket
 
HOST = "localhost"
PORT = 8080
 
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((HOST, PORT))
 
sock.sendall("Hello\n")
data = sock.recv(1024)
print "1)", data
 
if ( data == "olleH\n" ):
    sock.sendall("Bye\n")
    data = sock.recv(1024)
    print "2)", data
 
    if (data == "eyB}\n"):
        sock.close()
        print "Socket closed"