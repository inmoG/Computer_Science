import socket

hosts = ["127.0.0.1"]

for host in hosts:
    for port in range(0, 1024):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_TCP)
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        
        result = s.connect_ex((host, port)) # connect() 반환하는 결과값이 없어 조건 만족 X
        if result == 0:
            print(f"[*] {str(port)}open!")        
        else:
            print(f"{str(port)} close!")
            
        s.close()