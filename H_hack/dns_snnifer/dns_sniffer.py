#!/usr/bin/env python3
import scapy.all as scapy



def process_dns_packet(packet):
    if packet.haslayer(scapy.DNSQR):
       domain = packet[scapy.DNSQR].qname.decode()
       exclude_keywords = ['google', 'cloud','bing','static']
       if not any(keyword in domain for keyword in exclude_keywords):
            if domain not in domains_seen:
              domains_seen.add(domain)
              print(f"`[+]Dominio:{domain}")
         

def main():
  global domains_seen
  domains_seen = set()
  interface = "eth0"
  scapy.sniff(iface=interface, filter="udp port 53", store=False, prn=process_dns_packet)

if __name__ == '__main__':
    main()
    