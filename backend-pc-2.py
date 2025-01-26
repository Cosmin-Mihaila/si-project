import socket

ip_hash = {}

def start_server(host, port):
    server_socket = socket.socket(AF_INET, SOCK_DGRAM)
    server_socket.bind((host, port))
    print(f"Server listening on {host}:{port}")
    while True:
        message, client_address = server_socket.recvfrom(4096)
        print("REQUEST FROM ", client_address[0])
      
        if client_address[0] in ip_hash.keys():
          ip_hash[client_address[0]] += 1
        else:
          ip_hash[client_address[0]] = 1

        if ip_hash[client_address[0]] > 20:
          print("Too many requests from this IP")
          break



        if message == b"1234":
          print("PIN OK")
        else:
          print("INCORRECT")

        
        

# Configurare
host = "0.0.0.0"  # Ascultă pe toate interfețele
port = 3000  # Portul UDP pe care serverul ascultă

start_server(host, port)
