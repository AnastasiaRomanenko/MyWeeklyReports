import socket

PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    while True:
        message = input("Send smth to server: ")
        s.sendto(message.encode(), (SERVER, PORT))
