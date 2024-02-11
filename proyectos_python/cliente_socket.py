#!/usr/bien/env python3
import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_adress = ("localhost", 12345)
client_socket.connect(server_adress)

while True:
    mensaje = input("Escriba el mensaje a enviar: ")
    client_socket.send(mensaje.encode())
    data = client_socket.recv(1024)
    print("Recibido: ", data.decode())
    if mensaje == "exit":
        break
client_socket.close()