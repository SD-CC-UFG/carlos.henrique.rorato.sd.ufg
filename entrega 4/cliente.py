# Sistemas Distribuídos
# Alunos: Carlos Henrique Rorato Souza, Juliana de Melo Teixeira
#Resolucao da questao 1 da lista 1 com escalabilidade utilizando threads
#mandando mensagem atraves de objeto utilizando pickle
import socket
import sys
import pickle

class Data:
	def __init__(self):
		self.nome = ""
		self.cargo = ""
		self.salario = 0

def main():
    soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = "127.0.0.1"
    port = 14576

    try:
        soc.connect((host, port))
    except:
        print("Erro de conexao")
        sys.exit()

    while True:
		entrada = Data()
		print("Utilize Ctrl+Z para finalizar conexao")
		print ("Nome:")
		entrada.nome = raw_input()
		print ("Cargo (operador/programador):")
		entrada.cargo = raw_input()
		print ("Salario:")
		entrada.salario = raw_input()
		
		
		data_string = pickle.dumps(entrada)
		soc.send(data_string)
	
		message = soc.recv(1024)
	
		if not message:
			print ("Sem resposta do servidor")
		else:
			print (message)

    soc.send(b'--quit--')

if __name__ == "__main__":
    main()

