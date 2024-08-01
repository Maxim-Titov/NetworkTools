#!/usr/bin/env python3

import subprocess as sub_proc
import re
import random

sub_proc.call("clear", shell=True)
sub_proc.call("figlet MAC Changer | lolcat", shell=True)

interface = input("[ ] Enter interface: ")

one = f"{random.randint(0, 9)}{random.randint(0, 9)}"
two = f"{random.randint(0, 9)}{random.randint(0, 9)}"
three = f"{random.randint(0, 9)}{random.randint(0, 9)}"
four = f"{random.randint(0, 9)}{random.randint(0, 9)}"
five = f"{random.randint(0, 9)}{random.randint(0, 9)}"
six = f"{random.randint(0, 9)}{random.randint(0, 9)}"

macAddress = f"{one}:{two}:{three}:{four}:{five}:{six}"

def changeMac(interface, new_mac):
	print("[+] Changing MAC address for " + interface + " to " + new_mac)

	sub_proc.call(f"sudo ifconfig {interface} down", shell=True)
	sub_proc.call(f"sudo ifconfig {interface} hw ether {new_mac}", shell=True)
	sub_proc.call(f"sudo ifconfig {interface} up", shell=True)

def getCurrentMac(interface):
	ifconfig_res = sub_proc.check_output(["ifconfig", interface]).decode('utf-8')
	macSearchRes = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", ifconfig_res)

	if macSearchRes:
		return macSearchRes.group(0)
	else:
		print("\033[0;31;40m[-] Could not read MAC address.")

current_mac = getCurrentMac(interface)
	
if current_mac != None:
	print("Current MAC: " + current_mac)

	print("\n")

	changeMac(interface, macAddress)

	print("\n")

	current_mac = getCurrentMac(interface)

	if current_mac == macAddress:
		print("\033[0;32;40m[+] MAC address was successfully changed to: " + current_mac)
	else:
		print("\033[0;31;40m[-] MAC address did not get changed")
