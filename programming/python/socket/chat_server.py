import socketserver

class MyHandler(socketserver.BaseRequestHandler):
    users={}
    def handle(self):
        print(self.client_address)

        while True:
            self.request.send("채팅 닉네임을 입력하세요: ".encode())

            nickname = self.request.recv(1024).decode()
            print(nickname)
            if nickname in self.users:
                self.request.send("이미 등록된 닉네임입니다.\n".encode())
            else:
                self.users[nickname] = (self.request, self.client_address)

class ChatServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    pass

server = ChatServer(("", 12000), MyHandler)
server.serve_forever()
server.shutdown()
server.server_close()