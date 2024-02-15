import random
import string
import requests
    
url = 'http://localhost:7890/keylog'
length = 10
email = ''.join((random.choice(string.ascii_lowercase + string.digits) for i in range(length))) + "@gmail.com"
print("Email: "+ email + "\n")
username = ''.join((random.choice(string.ascii_letters + string.digits) for i in range(length)))
print("Username: "+ username + "\n")
first_letter_first_name = ''.join(random.choice(string.ascii_uppercase) for i in range(1))
other_letters_first_name =  ''.join(random.choice(string.ascii_lowercase) for i in range(5))  
first_letter_last_name = ''.join(random.choice(string.ascii_uppercase) for i in range(1))
other_letters_last_name =  ''.join(random.choice(string.ascii_lowercase) for i in range(5)) 
full_name = first_letter_first_name + other_letters_first_name + " " + first_letter_last_name + other_letters_last_name

print("Full name: "+ full_name + "\n")
phone_number = ''.join((random.choice(string.digits) for i in range(10)))
print("Phone number: "+ phone_number + "\n")

with open("email.txt", "w") as file:
        file.write(email + "\n")
        file.close()
with open("username.txt", "w") as file:
        file.write(username + "\n")
        file.close()
with open("full_name.txt", "w") as file:
        file.write(full_name + "\n")
        file.close()
with open("phone_number.txt", "w") as file:
        file.write(phone_number + "\n")
        file.close()

responseEmail = requests.post(url, data=email)
print("\n" + responseEmail.text)
responseUsername = requests.post(url, data=username)
print("\n" + responseUsername.text)
responseFullName = requests.post(url, data=full_name)
print("\n" + responseFullName.text)
responsePhoneNumber = requests.post(url, data=phone_number)
print("\n" + responsePhoneNumber.text)