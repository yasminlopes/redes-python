import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(('127.0.0.1', 9999))

msg, ender = s.recvfrom(1024)

print(msg.decode('utf-8'))
s.sendto("Olá Cliente!".encode('utf-8'), ender)

