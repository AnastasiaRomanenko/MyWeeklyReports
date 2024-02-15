from flask import Flask, request

app = Flask(__name__)
@app.route('/', methods=['GET'])
def home():
    return 'Home page'

@app.route('/email', methods=['GET'])
def email():
    with open("email.txt", "r") as file:
        email = file.read()
        file.close()
    return 'Email: ' + email 

@app.route('/username', methods=['GET'])
def username():
    with open("username.txt", "r") as file:
        username = file.read()
        file.close()
    return 'Username: ' + username 

@app.route('/full_name', methods=['GET'])
def full_name():
    with open("full_name.txt", "r") as file:
        full_name = file.read()
        file.close()
    return 'Full name: ' + full_name 

@app.route('/phone_number', methods=['GET'])
def phone_number():
    with open("phone_number.txt", "r") as file:
        phone_number = file.read()
        file.close()
    return 'Phone number: ' + phone_number 

if __name__ == "__main__":
    app.run(port=7890)
