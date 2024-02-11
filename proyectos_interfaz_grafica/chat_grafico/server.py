#!/usr/bin/env python3

import socket
import threading

def handle_client(client_socket, clients, usernames):#funcion para manejar los clientes que se conectan cada uno en un hilo
   user = client_socket.recv(1024).decode()#recibe el nombre de usuario del cliente
   usernames[client_socket] = user#agrega el nombre de usuario a la lista de nombres de usuario
   print(f"[+]Nombre de usuario del cliente:{user}")

   for client in clients:
         if client is not client_socket:
             client.sendall(f"{user} se ha conectado al chat".encode())
   while True:
        try:
            mensaje = client_socket.recv(1024).decode()#recibe el mensaje del cliente
            if not mensaje:
                break
            if mensaje == "¡usuario":
                client_socket.sendall(f"[+]Los usuarios conectados son:{", " .join(usernames.values())}".encode())#envia el mensaje al cliente
                continue#vuelve al inicio del bucle
            for client in clients:
                if client is not client_socket:
                    client.sendall(f"{user} --> {mensaje}".encode())#envia el mensaje a todos los clientes
           
        except:
               break
        
   client_socket.close()     
   clients.remove(client_socket)
   del usernames[client_socket]




def server_program():#funcion principal del servidor
    host = "localhost"
    port = 5000

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1) #para que no de error de que el puerto esta en uso
    server_socket.bind((host, port))
    server_socket.listen()
    
    print(f"[+]Server esta esperando conexiones <<---")
    
    clients = []
    usernames = {}
    while True:
        client_socket, client_address = server_socket.accept()#acepta la conexion del cliente
        clients.append(client_socket)
        print(f"[+]Conexion establecida con:{client_address}")
        thead = threading.Thread(target=handle_client, args=(client_socket, clients, usernames))
        thead.daemon = True #para que se cierre el hilo cuando se cierre el programa
        thead.start()
if __name__ == "__main__":
    server_program () 