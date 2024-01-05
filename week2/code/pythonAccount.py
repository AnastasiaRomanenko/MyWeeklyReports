import os

def writeToFile(filename, age, password):
    file = open(filename, 'w')
    file.write(age + ",")
    file.write(password)
    file.close()

def readFromFile(filename):
    file = open(filename, 'r')
    text = file.read()
    file.close()
    return text

def getUserInput():
    name = input("\033[31mWhat is your name? \033[0m")
    return name

filename = getUserInput() + ".txt"
if os.path.exists(filename):
    content = readFromFile(filename)
    age, password = content.split(',')
    userEnterPassword = input("\033[32mEnter your password: \033[0m")
    while userEnterPassword != password:
        userEnterPassword = input("\033[33mThe password is incorrect! Enter it again: \033[0m")

    print("\033[34mData inside the file: \033[0m")
    print("\033[35m"+age+"\033[0m")
else:
    password = input("\033[36mSet your password: \033[0m")
    age = input("\033[35mEnter your age: \033[0m")
    writeToFile(filename, age, password)
    print("\033[34m"+age+"\033[0m")