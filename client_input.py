import socket

port = 2500
BUFFSIZE = 1024

sock = sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
msg = "Hello"
sock.sendto(msg.encode(), ("localhost", port))

while True:
    data, addr = sock.recvfrom(BUFFSIZE)
    print("Server: ", data.decode())
    msg = input("Sending Message: ")
    sock.sendto(msg.encode(), addr)
