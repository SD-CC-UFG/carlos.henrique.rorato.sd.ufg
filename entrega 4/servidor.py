# Sistemas Distribuídos
# Alunos: Carlos Henrique Rorato Souza, Juliana de Melo Teixeira
#Resolucao da questao 1 da lista 1 com escalabilidade utilizando threads
#mandando mensagem atraves de objeto utilizando pickle
import socket
import sys
import traceback
from threading import Thread
import pickle

class Data:
	def __init__(self):
		self.nome = ""
		self.cargo = ""
		self.salario = 0

def main():
    start_server()


def start_server():
    host = "127.0.0.1"
    port = 14576  #porta definida

    soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    soc.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) 
    print("Socket criado")

    try:
        soc.bind((host, port))
    except:
        print("Bind falhou. Error : " + str(sys.exc_info()))
        sys.exit()

    soc.listen(5)   
    print("Socket escutando")

    while True:
        connection, address = soc.accept()
        ip, port = str(address[0]), str(address[1])
        print("Conectado com " + ip + ":" + port)

        try:
            Thread(target=client_thread, args=(connection, ip, port)).start()
        except:
            print("Thread nao iniciou.")
            traceback.print_exc()

    sock.close()


def client_thread(connection, ip, port, max_buffer_size = 5120):
    is_active = True

    while is_active:
        client_input = receive_input(connection, max_buffer_size)

        if "--QUIT--" in client_input:
            connection.close()
            print("Conexao " + ip + ":" + port + " fechada")
            is_active = False
        else:
            connection.send(client_input)


def receive_input(connection, max_buffer_size):
    client_input = connection.recv(max_buffer_size)
    client_input_size = sys.getsizeof(client_input)

    if client_input_size > max_buffer_size:
        print("O input eh maior que o esperado {}".format(client_input_size))

    decoded_input = pickle.loads(client_input)
    result = process_input(decoded_input)

    return result


def process_input(entrada):
	novo_sal = float(entrada.salario)
	if entrada.cargo == 'operador':
		novo_sal = novo_sal + (0.2*novo_sal)
	elif entrada.cargo == 'programador':
		novo_sal = novo_sal + (0.18*novo_sal)
	msg = "Novo salario: "+str(novo_sal)
	return msg

if __name__ == "__main__":
    main()
