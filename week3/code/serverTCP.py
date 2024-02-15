import socket
import sys
import pkg_resources

PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)

try:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((SERVER, PORT))
        s.listen()
        while True:
            conn, addr = s.accept()
            with conn:
                print(f"Connected by {addr}")
                while True:
                    data = conn.recv(1024)
                    if (len(data) == 0):
                        break
                    print("Get smth from client: " + data.decode())
                    conn.sendall(data)

except KeyboardInterrupt:
    sys.exit(0)