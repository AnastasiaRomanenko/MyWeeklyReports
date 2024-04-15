from flask import Flask, request, send_file

app = Flask(__name__)

@app.route('/')
def home():
    return 'Home page'

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form.get('name')
        surname = request.form.get('surname')
        username = request.form.get('username')
        password = request.form.get('password')

        response_html = f"""
        <h1>Your data:</h1>
        <p>Name: {name}</p>
        <p>Surname: {surname}</p>
        <p>Username: {username}</p>
        <p>Password: {password}</p>
        """
        return response_html
    else:
        response = send_file('register.html', mimetype='text/html')
        response.headers['Content-Type'] = 'text/html'
        return response

if __name__ == '__main__':
    app.run(port=5500)
