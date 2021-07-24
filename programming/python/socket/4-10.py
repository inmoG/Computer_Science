import socket

host = "www.google.com"
port = 80

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_TCP)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

address = socket.gethostbyname(host)
sock.connect((address, port))

print(f"socket connected to {host} on {address}")

message = b"GET / HTTP/1.1\r\n\r\n" # \r\n\r\n HTTP 헤더 끝 부분이다.

sock.sendall(message)

data = sock.recv(65565) # 응답 페이지 내용을 recv() 로 수신

print(data)
sock.close()