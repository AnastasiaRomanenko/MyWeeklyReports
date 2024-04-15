import glob
import os
import socket
import threading
import sys
import random
from datetime import datetime
import time

usernameS = ""
usernameC = ""
mode = sys.argv[2] 
forbidden_words = ["banana", "apple", "orange", "grape", "kiwi"]
check = True

if mode == 'server':
    usernameS = sys.argv[1]
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    port = int(sys.argv[3])
    server.bind(('localhost', port))
    server.listen(5)
    with open("server.txt", 'w+') as file:
        file.write(usernameS) 

elif mode == 'client':
    usernameC = sys.argv[1]
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = sys.argv[3].split(':')[0]
    port = int(sys.argv[3].split(':')[1])
    client.connect((host, port))
    with open("client.txt", 'w+') as file:
        file.write(usernameC)
    with open(usernameC+".txt", 'a+') as file:
        iAmClient = f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}]> User {usernameC} connected to the chat.\n"
        file.write(iAmClient)


def handle_connection(conn, username, filename, assigned_word):
    global check
    with open(filename+".txt", 'a+') as file:
        while True:
            data = conn.recv(1024).decode('utf-8')
            if data:
                if(check == True and username != filename):
                    message=f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}]> {data}\n"
                    check = False
                else: 
                    for word in data.split():
                        if(username != filename and word.lower() == assigned_word):
                            print(assigned_word)
                            message=f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}]> The user guessed the word!\n"
                            break
                        elif(username == filename and word.lower() in forbidden_words):
                            message=f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}]> The user used a forbidden word!\n"
                            break
                        else: 
                            message=f"{username} [{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}]> {data}\n"
                print(message)
                file.write(message)
                file.flush()

if mode == 'server':

    while True:
        if os.path.exists("client.txt"):
            time.sleep(0.5)
            with open("client.txt", 'r') as file:
                usernameC = file.read()
                os.remove("client.txt")
                conn, addr = server.accept()
                with open(usernameC+".txt", 'r') as f:
                    first_line = f.readline()
                    print(first_line)
                
                assigned_word = random.choice(forbidden_words)

                with open("word.txt", 'w+') as f:
                    f.write(assigned_word)
                
                threading.Thread(target=handle_connection, args=(conn, usernameC, usernameC, assigned_word)).start()
                conn.sendall(f"The user needs to guess the word: {assigned_word}.".encode('utf-8'))

                while True:
                    messageS = input()
                    conn.sendall(messageS.encode('utf-8'))

elif mode == 'client':

    with open("server.txt", 'r') as file:
        usernameS = file.read()
        os.remove("server.txt")
    
    while True:
        if os.path.exists("word.txt"):
            with open("word.txt", 'r') as file:
                assigned_word = file.read()
                os.remove("word.txt")
                break
    
    threading.Thread(target=handle_connection, args=(client, usernameS, usernameC, assigned_word)).start()
    
    while True:
        message = input()
        client.sendall(message.encode('utf-8'))    

if mode == 'server':
    server.close()
elif mode == 'client':
    client.close()