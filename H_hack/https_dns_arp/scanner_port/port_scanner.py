#!/usr/bin/env python3

import socket
import argparse
import sys
import signal
from concurrent.futures import ThreadPoolExecutor#para que sea mas rapido el escaneo y maneja la cantidad de hilos que se van a ejecutar
from termcolor import colored

open_socket = []

def signal_handler(signal, frame):#para que cuando se presione ctrl+c se cierren los sockets abiertos
    print(colored("\n[!!] Saliendo del programa...", 'red'))
    for s in open_socket:
            s.close()  
    sys.exit(1)
signal.signal(signal.SIGINT, signal_handler) #para que cuando se presione ctrl+c se cierren los sockets abiertos


def get_arguments():
    parser = argparse.ArgumentParser(description='Port Scanner, by H_hack')
    parser.add_argument('-t', '--target', dest='target',required=True, help='Victim target to scan ports Ex:(-t 192.168.1.1)')#si pongo recuaret=true no tengo que poner if options.target is None or options.port is None:
    parser.add_argument('-p', '--port', dest='port',required=True, help=' Port renge to scan Ex:(-p 1-100)')
    options = parser.parse_args()
    return options.target, options.port


def create_socket():
   
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.5)#tiempo de espera para que no se quede colgado
    open_socket.append(s)
    return s

def port_scanner(port,host):
  s = create_socket()    

  try:
        
        s.connect((host, port))
        s.sendall(b'HEAD / HTTP/1.1\r\n\r\n')
        response = s.recv(1024).decode()
      
        if response:
            print(colored(f"La respuesta del puerto {port} es: {response}", 'green'))
      
  except (socket.timeout, ConnectionRefusedError):
        pass
  finally:
        s.close()


def scan_ports(ports,target):

    with ThreadPoolExecutor(max_workers=100) as executor:
        for port in ports:
            executor.submit(port_scanner, port,target)

def parse_port(port_str):
    if '-' in port_str:
        start, end = map(int, port_str.split('-'))
        return range(start, end + 1)
    elif "," in port_str:
        return map(int, port_str.split(','))
    else: 
        return (int(port_str),)

def main():
    target, port_str = get_arguments()
    ports = parse_port(port_str) 
    scan_ports(ports, target)

if __name__ == '__main__':
    main()
 
