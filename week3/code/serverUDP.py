import socket
import sys

PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)

# try:
with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    s.bind((SERVER, PORT))
    print(f"Connected by {ADDR}")
    while True:
        data, addr = s.recvfrom(1024)
        print("Get smth from client: " + data.decode())