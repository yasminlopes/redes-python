import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("127.0.0.1", 9999))

s.send("Olá servidor".encode('utf-8'))
print(s.recv(1024).decode('utf-8'))
s.send("Tchau servidor".encode('utf-8'))
print(s.recv(1024).decode('utf-8'))


