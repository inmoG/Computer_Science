import socket
from threading import Thread

def recv_message(sock):
    while True:
        msg = sock.recv(1024)
        print(msg.decode())



sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(("127.0.0.1", 12000))

th = Thread(target=recv_message, args=(sock, ))
th.daemon = True
th.start()

while True:
    msg = input("입력 : ")
    sock.send(msg.encode())

    if msg=="/bye":
        break

sock.close()