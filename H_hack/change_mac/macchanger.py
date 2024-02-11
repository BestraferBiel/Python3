#!/usr/bin/env python3

import argparse
import subprocess
import re
import platform


def obtener_mac_actual(interface):
    if platform.system().lower() == "windows":
        result = subprocess.run(['netsh', 'interface', 'show', 'interface', interface], stdout=subprocess.PIPE, text=True)
        match = re.search(r'MAC Address: (.+)', result.stdout)
        if match:
            return match.group(1)
    elif platform.system().lower() == "linux":
        result = subprocess.run(['ifconfig', interface], stdout=subprocess.PIPE, text=True)
        match = re.search(r'HWaddr\s+(\S+)', result.stdout)
        if match:
            return match.group(1)
    return None

def get_arguments():
    parser = argparse.ArgumentParser(description='Herramienta para cambiar la dirección MAC, by H_hack')
    parser.add_argument('-i', '--interface', dest='interface', required=True, help='Hay que brindar la interfaz a cambiar')
    parser.add_argument('-m', '--MAC', dest='mac', required=True, help='Hay que brindar la nueva dirección MAC ej:(-m 00:11:22:33:44:55)')
    
    # Modificamos el método de parseo de argumentos para permitir que la interfaz contenga espacios
    options = parser.parse_args()
    
    # Puedes acceder a los valores con options.interface y options.mac
    return options.interface, options.mac

def validar_argumentos(interface):
        
        if platform.system().lower() == "windows":
            result = subprocess.run(['ipconfig'], stdout=subprocess.PIPE, text=True)
            interfaces = re.findall(r'(?<=\bAdapter ).*(?=:)', result.stdout)
            return interface in interfaces
        elif platform.system().lower() == "linux":
            result = subprocess.run(['ifconfig'], stdout=subprocess.PIPE, text=True)
            interfaces = re.findall(r'^\S+', result.stdout, flags=re.MULTILINE)
            return interface in interfaces
        return False


   

def change_mac_adress(interface, mac):
    if validar_argumentos(interface) == True:
      
        subprocess.run(['netsh', 'interface', 'set', 'interface', interface, 'admin=disable'])
        subprocess.run(['netsh', 'interface', 'set', 'interface', interface, 'newmac=' + mac])
        subprocess.run(['netsh', 'interface', 'set', 'interface', interface, 'admin=enable'])
        return (f"La direccion MAC ha sido cambiada exitosamente a {mac}")
   
    else:

        subprocess.run(['ifconfig', interface, 'down'])
        subprocess.run(['ifconfig', interface, 'hw', 'ether', mac])
        subprocess.run(['ifconfig', interface, 'up'])
        return (f"La direccion MAC ha sido cambiada exitosamente a {mac}")




def main():
    interface, mac = get_arguments()
    #print(f"La interface a cambiar es: {interface} y la nueva direccion MAC es: {mac}")
   # change_mac_adress(interface, mac)
    #mac_actual = obtener_mac_actual("Wi-Fi")
    validar = validar_argumentos(interface)
    print(validar)

if __name__ == '__main__':
    main()




