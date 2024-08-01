#!/usr/bin/env python3

import subprocess as sub_proc

sub_proc.call("clear", shell=True)
sub_proc.call("figlet netTools | lolcat", shell=True)

print("1. MAC changer\n"
      "2. Network scanner\n"
      "3. ARP spoofing\n"
      "4. DNS spoofing\n"
      "5. Packet sniffer\n"
      "6. Bruteforce")
select = input(">>> ")

if select == "1":
    from tools import macChenger
elif select == "2":
    from tools import networkScanner
elif select == "3":
    from tools import arpSpoof
elif select == "4":
    from tools import dnsSpoof
elif select == "5":
    from tools import packetSniffer
elif select == "6":
    from tools import bruteforce
else:
    print("Number out of list")
