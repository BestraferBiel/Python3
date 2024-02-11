#!/usr/bin/env python3
import scapy.all as scapy
import argparse


def get_arguments():
    parser = argparse.ArgumentParser(description='ARP scanner, by H_hack')
    parser.add_argument('-t', '--target', dest='target',required=True, help='Target IP / IP range. Ex:(-t')
    options = parser.parse_args()
    return options.target


def scan(ip):
    arp_packet = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst='ff:ff:ff:ff:ff:ff')    
    
    arp_packet = broadcast/arp_packet
    answered,unanswered  = scapy.srp(arp_packet, timeout=1, verbose=False)
   
    response = answered.summary()
    if response:
        print('IP\t\t\tMAC Address\n-----------------------------------------')
        print(response)
def main():
    target_ip = get_arguments()
    scan(target_ip)

if __name__ == "__main__":
    main()
