import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

s.sendto("Olá Servidor".encode('utf-8'), ("127.0.0.1", 9999))
print(s.recvfrom(1024)[0].decode('utf-8'))