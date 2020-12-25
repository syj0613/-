import socket

port = 2500
BUFFSIZE = 1024

sock = sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
msg = "Hello"
sock.sendto(msg.encode(), ("localhost", port))
data, addr = sock.recvfrom(BUFFSIZE)
print("Server: ", data.decode())
