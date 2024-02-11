
import subprocess
import platform
import re

def obtener_mac_actual(interfaz):
    if platform.system().lower() == "windows":
        result = subprocess.run(['netsh', 'interface', 'show', 'interface', interfaz], stdout=subprocess.PIPE, text=True)
        match = re.search(r'MAC Address: (.+)', result.stdout)
        if match:
            return match.group(1)
    elif platform.system().lower() == "linux":
        result = subprocess.run(['ifconfig', interfaz], stdout=subprocess.PIPE, text=True)
        match = re.search(r'HWaddr\s+(\S+)', result.stdout)
        if match:
            return match.group(1)
    return None

def validar_interfaz(interfaz):
    if platform.system().lower() == "windows":
            result = subprocess.run(['ipconfig'], stdout=subprocess.PIPE, text=True)
            interfaces = re.findall(r'(?<=\bAdapter ).*(?=:)', result.stdout)
            return print(interfaces)                                                                       #interfaces = re.findall(r"Adaptador[^:]+:[\s\S]*?(?=(?:Adaptador|$))", result.stdout)
                    
                                                                   #return print(interfaces[6])
    
   # elif platform.system().lower() == "linux":
    #    result = subprocess.run(['ifconfig'], stdout=subprocess.PIPE, text=True)
     #   interfaces = re.findall(r'^\S+', result.stdout, flags=re.MULTILINE)
      #  return interfaz in interfaces
    return False

def cambiar_mac(interfaz, nueva_mac):
    if platform.system().lower() == "windows":
        subprocess.run(['netsh', 'interface', 'set', 'interface', interfaz, 'admin=disable'])
        subprocess.run(['netsh', 'interface', 'set', 'interface', interfaz, 'newmac=' + nueva_mac])
        subprocess.run(['netsh', 'interface', 'set', 'interface', interfaz, 'admin=enable'])
    elif platform.system().lower() == "linux":
        subprocess.run(['ifconfig', interfaz, 'down'])
        subprocess.run(['ifconfig', interfaz, 'hw', 'ether', nueva_mac])
        subprocess.run(['ifconfig', interfaz, 'up'])

# Ejemplo de uso
interfaz_usuario = input("Introduce el nombre de la interfaz de red: ")
ok ="VMnet1"
print(validar_interfaz(ok))

#if validar_interfaz(interfaz_usuario):


    # Almacena la dirección MAC actual
   # mac_original = obtener_mac_actual(interfaz_usuario)
    #print(f"La dirección MAC actual de {interfaz_usuario} es: {mac_original}")
    
   # nueva_mac_usuario = input("Introduce la nueva dirección MAC: ")
    #cambiar_mac(interfaz_usuario, nueva_mac_usuario)
    #print(f"La dirección MAC de {interfaz_usuario} ha sido cambiada a {nueva_mac_usuario}")

    # Para revertir el cambio y volver a la dirección MAC original
    #restaurar = input("¿Deseas restaurar la dirección MAC original? (Sí/No): ")
    #if restaurar.lower() == "si":
     #   cambiar_mac(interfaz_usuario, mac_original)
      #  print(f"La dirección MAC de {interfaz_usuario} ha sido restaurada a {mac_original}")
#else:
    #print(f"La interfaz {interfaz_usuario} no es válida.")
