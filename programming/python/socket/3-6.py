import socket
host = "127.0.0.1"

port = 12345

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
# AF_INET : IP / SOCK_DGRAM : UDP / IPPROTO_UDP : UDP
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# sock.bind(host, port) UDP 클라이언트는 bind()함수를 이용한 연동과정이 불필요하다.

print(sock)
sock.close()