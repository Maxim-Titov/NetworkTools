#!/usr/bin/env/ python3

import subprocess as sub_proc
import scapy.all as scapy

# def scan(ip):
# 	scapy.arping(ip)

sub_proc.call("clear", shell=True)
sub_proc.call("figlet Network Scanner | lolcat", shell=True)
target = input("[ ] Enter target IP: ")

def scan(ip):
	arpRequest = scapy.ARP(pdst = ip)
	broadcast = scapy.Ether(dst = "ff:ff:ff:ff:ff:ff")
	arpRequestBroadcast = broadcast/arpRequest

	answered_list = scapy.srp(arpRequestBroadcast, timeout=1, verbose=False)[0]
	
	clients_list = []
	for element in answered_list:
		clients_dict = {"ip": element[1].psrc, "mac": element[1].hwsrc}
		clients_list.append(clients_dict)
	
	return clients_list

def print_result(result_list):
	print("IP\t\t\tMAC Address\n-----------------------------------------")
	for client in result_list:
		print(client["ip"] + "\t\t" + client["mac"])

scan_result = scan(target)
print_result(scan_result)
