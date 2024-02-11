#!/usr/bin/env python3

import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_adress = ("localhost", 12345)
server_socket.bind(server_adress)
server_socket.listen(1)#1 es el numero de conexiones que acepta el servidor

while True:
    print("Esperando conexiones...")
    client_socket, client_adress = server_socket.accept()
    print("Conexion desde: ", client_adress)
    while True:
        data = client_socket.recv(1024)
        print("Recibido: ", data.decode())
        if data:
            client_socket.send("Hola cliente:".encode())
        else:
            break
    client_socket.close()