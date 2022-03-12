import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('localhost', 9999))

s.listen()

while True:
    cliente, ender = s.accept()

    print(f"Conectado ao {ender}")

    print(cliente.recv(1024).decode('utf-8'))
    cliente.send("Enviando um Olá para o Cliente!".encode('utf-8'))

    print(cliente.recv(1024).decode('utf-8'))
    cliente.send("Tchau, tchau! Encerrando a conexão.".encode('utf-8'))

    cliente.close()





