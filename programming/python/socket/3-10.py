import socket
host = "127.0.0.1"
port = 12345

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_TCP)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

sock.connect((host,port))

# connect 함수는 udp 클라이언트에 없다  해당함수는 tcp 서버 측 accept 함수와 대응 관계를 이루면서 일련의 3단계 연결 설정을 수행한다.

print(sock)
sock.close()