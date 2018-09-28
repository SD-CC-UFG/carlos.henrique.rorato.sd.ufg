// Sistemas Distribuídos
// Aluno: Carlos Henrique Rorato Souza
// Comunicação cliente/servidor com linguagens diferentes
// Módulo Servidor - JAVA
// Esta implementação utiliza sockets

import java.io.*;
import java.net.*;
 
class JavaServer {
    public static void main(String args[]) throws Exception {
        String fromClient;
        String toClient;
    
        //Estabelecendo a conexão com o socket
        ServerSocket server = new ServerSocket(8080);
        System.out.println("wait for connection on port 8080");
 
        boolean run = true;
        while(run) { 
            Socket client = server.accept(); //aceita o pedido de conexão do cliente
            System.out.println("got connection on port 8080");

            BufferedReader in = new BufferedReader(new InputStreamReader(client.getInputStream()));
            PrintWriter out = new PrintWriter(client.getOutputStream(),true);
 
            fromClient = in.readLine();
            System.out.println("recebido: " + fromClient);
 
            if(fromClient.equals("Hello")) {
                toClient = "olleH";
                System.out.println("send olleH");
                out.println(toClient);
                fromClient = in.readLine();
                System.out.println("received: " + fromClient);
 
                if(fromClient.equals("Bye")) {
                    toClient = "eyB";
                    System.out.println("send eyB");
                    out.println(toClient);
                    client.close();
                    run = false;
                    System.out.println("socket closed");
                }
            }
        }
        System.exit(0);
    }
}