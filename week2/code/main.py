import os
import sys
sys.path.append('./hectIO') 
import hectIO

def writeToFile(filename, content):
    file = open(filename, 'w')
    file.write(content)
    file.close()

def readFromFile(filename):
    file = open(filename, 'r')
    text = file.read()
    file.close()
    return text

def getUserInput():
    name = input("\033[31mEnter a filename: \033[0m")
    return name


filename = getUserInput()
if os.path.exists(filename):
    print("\033[32mThe content of the file: \033[0m")
    content = readFromFile(filename)
    print("\033[33m"+content+"\033[0m")
else:
    print("\033[34mCreating a random string:\033[0m")
    length = 10
    content = hectIO.getRandomStr(length)
    writeToFile(filename, content)
    print("\033[35m"+content+"\033[0m")
