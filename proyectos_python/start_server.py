#!/usr/bin/env python3

import socket

def star_server():
    host = "localhost"
    port = 12345
    
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((host, port))
        server_socket.listen(1)
        print(f"Servidor escuchando en {host}:{port}...")
        client_socket, client_address = server_socket.accept()
        print(f"Cliente conectado desde: {client_address}")
        while True:
            data = client_socket.recv(1024)
            print("Recibido: ", data.decode())
            if data.decode() == "exit":
                break
            mensaje = input("Respondiendo desde el servidor: ")
            client_socket.send(mensaje.encode())
        client_socket.close()
        print("Cliente desconectado...")

star_server()         