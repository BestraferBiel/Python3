#!/usr/bin/env python3
import threading
import socket

class ClientThread(threading.Thread):
    def __init__(self, client_socket, client_address):
        threading.Thread.__init__(self)# para que se ejecute el init de la clase padre
        self.client_socket = client_socket
        self.client_address = client_address

    def run(self):
        with self.client_socket as sock:
            while True:
                print(f"[*] Conexion con {self.client_address[0]}:{self.client_address[1]}")
                data = sock.recv(1024)
                if data.decode() == "exit":
                    break
                print(f"[*] Recibido: {data.decode('utf-8')}")
                mensaje = input("Mensaje para enviarle cliente: ")
                sock.sendall(mensaje.encode())
            print(f"[-] Conexion con {self.client_address[0]}:{self.client_address[1]} terminada")
            sock.close()

HOST = "localhost"
PORT = 12345

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)# para que no de error de que el puerto esta en uso (reutilizarlo)
    server_socket.bind((HOST, PORT))
    print(f"[*] Escuchando en:{HOST}:{PORT}")    
    while True:
        server_socket.listen()
        client_socket, client_address = server_socket.accept()
        new_thread = ClientThread(client_socket, client_address)  
        new_thread.start()

