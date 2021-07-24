import socket

host = "www.google.com"
port = 80

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_TCP)

address = socket.gethostbyname(host) # get to ip
sock.connect((address, port)) # connect google

print(f"socket connected to {host} on {address}")
sock.close()