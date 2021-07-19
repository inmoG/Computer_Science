import socket

host = "127.0.0.1"
port = 12345

parent = socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_TCP) 
# AF_INET : IP / SOCK_STREAM : TCP / IPPROTO_TCP : TCP
# TCP/IP 기반 소켓 객체 생성 이때, 소켓 객체 parent는 부모 프로세스

parent.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

parent.bind((host, port))

parent.listen(10)
# listen 함수는 UDP 서버에는 없다. 3단계 연결 설정에 따라 동작하는 TCP 클라이언트로부터 연결 요청을 기다리겠다는 의미다. 이때 listen()함수 인자 10이 의미하는 바는
# 10대의 TCP 클라이언트 대상으로 동시 접속이 가능하다는 의미

(child, address) = parent.accept()
#UDP 소켓서버에는 없다. 해당 함수는 3단계 연결 수행 뒤 새로운 소켓객체 child와 주소(IP, 포트)를 튜플 타입으로 반환한다. 이때 accept()함수 실행까지는 부모 프로세서인 소켓 객체
# parent가 일련 작업 수행, accept()함수 실행 이후부터는 자식 프로세스인 소켓 객체 child가 일련의 작업을 수행한다 이 방식을 다중할당 방식이라 함

print(parent)
print(child)

child.close() # 자식 프로세스 소켓 객체 종료
parent.close() # 부모 프로세스 소켓 객체 종료