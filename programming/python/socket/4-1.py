import socket 

host = "127.0.0.1"
port = 12345
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

sock.bind((host, port))

(data, address) = sock.recvfrom(65565)
print(f"received{len(data)} bytes from {address}")

sock.close()
