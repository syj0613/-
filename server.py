import socket

port = 2500
BUFFER = 1024

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(("", port))
print("접속 대기중")

while True:
    data, addr = sock.recvfrom(BUFFER)
    print("Received Message: ", data.decode())
    print(addr)
    sock.sendto(data, addr)
    