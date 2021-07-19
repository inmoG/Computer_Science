import socket

host = "localhost"
# IP주소를 문자열 타입으로 설정
port = 12345
# 1024번 이후 포트 중 임의의 번호를 정수로 설정
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
#UDP/IP 기반의 소켓 객체 sock 생성
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
#setsockopt() 함수는 소켓 객체를 종료하자마자 해당 포트를 재사용하도록 허용하겠다는 설정. 선택 사항이지만 가급적 설정하는 것이 좋음
sock.bind((host, port))
#bind()함수를 이용해 IP, 포트 연동, 해당 함수를 이용해 localhost에서 12345번 포트를 활성화 시킨 udp 서버를 생성하겠다는 설정이다. 이때 
# bind()함수 인자는 (host, port)처럼 튜플 타입이다.
print(sock)
# 소켓 객체 sock 내용 출력
sock.close()
# 소켓 객체 생성한 뒤 처리 과정이 끝났으면 close() 함수 이용해 객체를 종료해야 함.