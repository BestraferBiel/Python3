#!/usr/bin/env python3

import argparse
import signal
from termcolor import colored
import subprocess
import sys
import platform
from concurrent.futures import ThreadPoolExecutor

def signal_handler(signal, frame):#para que cuando se presione ctrl+c se cierren los sockets abiertos
    print(colored("\n[!!] Saliendo del programa...", 'red'))
    sys.exit(1)
signal.signal(signal.SIGINT, signal_handler) #para que cuando se presione ctrl+c se cierren los sockets abiertos


def get_arguments():
    parser = argparse.ArgumentParser(description='Herramienta para descubrir hosts activos en una red(ICMP), by H_hack')
    parser.add_argument('-t', '--target', dest='target',required=True, help='Host o rango de red a escanear Ex:(-t 192.168.1.1-100)')
    options = parser.parse_args()
    return options.target


def formato(target_str):
    #192.168.1.1-100
   
        target_splited = target_str.split('.') #['192', '168', '1', '1-100']
        first_three_octets = '.'.join(target_splited[:3]) #192.168.1
        if len(target_splited) == 4:#si es una ip
             if '-' in target_splited[3]:#si es un rango de ips
                range_last_octet = target_splited[3].split('-')#['1', '100']
                start = int(range_last_octet[0])#1
                end = int(range_last_octet[1])#100
                return [f'{first_three_octets}.{last_octet}' for last_octet in range(start, end + 1)]
             else:
                return [target_str]
        else:
             print(colored("[-] El formato de la ip no es correcto", 'red'))

def host_discovery(target_final):
    
        try:

          if platform.system().lower() == "windows":
             # En sistemas Windows, usa el parámetro -n para el número de paquetes
              ping = subprocess.run(['ping', '-n', '1', target_final], timeout=0.5, stdout=subprocess.DEVNULL)#stdout=subprocess.DEVNULL para que no se muestre por pantalla
              if ping.returncode == 0:
                    print(colored(f"[+] Host {target_final} activo", 'green'))
          else:
             # En sistemas basados en Unix, usa el parámetro -c para el número de paquetes
             subprocess.run(['ping', '-c', '1', target_final], timeout=0.5, stdout=subprocess.DEVNULL)#stdout=subprocess.DEVNULL para que no se muestre por pantalla
             if ping.returncode == 0:
                 print(colored(f"[+] Host {target_final} activo", 'green'))
        except subprocess.TimeoutExpired:
            pass

def hilo (target_final):
    with ThreadPoolExecutor(max_workers=100) as executor:
        for ip in target_final:
            executor.submit(host_discovery, target_final=ip)

def main():
 target_str = get_arguments()
 targer_final = formato(target_str)
 hilo(targer_final)



if __name__ == '__main__':
        main()