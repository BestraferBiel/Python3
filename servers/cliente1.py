#!/usr/bin/env python3

import socket


def start_client():
    HOST = "localhost"
    PORT = 12345
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect((HOST, PORT))
        while True:
            msg = input("Mensaje: ")
            client_socket.sendall(msg.encode())
            if msg == "exit":
                break
            data = client_socket.recv(1024)
            print(f"[*] Recibido desde el server : {data.decode('utf-8')}")

start_client()