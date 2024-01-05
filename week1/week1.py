import random
# declare variables
name = "Anastasia"
ageStr = '18'
#Convert str to int
age = int(ageStr)
#print them
print(name)
print(age)
#Read string from the terminal and print to the screen
name = input("Enter your name: ")
print("Hello", name)
#Generate random number
random_num = random.randint(1, 10)
#take input from user, make it int 
num = int(input("Guess the number from 1 to 10: "))
#compare with your random number
while num != random_num:
    #If they wouldn't match, mass with the user
    num = int(input("Guess the number again: "))
print("You guessed it!")