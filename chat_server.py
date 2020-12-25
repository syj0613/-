import socket

port = 2500
BUFFSIZE = 1024

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('', port))

print("접속 대기중")

while True:
    print("<- ", end='')
    data, addr = sock.recvfrom(BUFFSIZE)
    print(data.decode())

    resp = input("-> ")
    sock.sendto(resp.encode(), addr)