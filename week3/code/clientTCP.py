import socket

PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((SERVER, PORT))
    while(True):
        message = input("Send smth to server: ")
        s.sendall(message.encode())
        data = s.recv(1024)
