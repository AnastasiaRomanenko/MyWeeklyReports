from flask import Flask, request, redirect, render_template, send_file, url_for
import json
import random
import string

url = Flask(__name__)

file = "templates/url.json"

@url.route('/')
def home():
    return 'Home page'

@url.route('/shorten', methods=['POST', 'GET'])
def shorten():
    if request.method == 'POST':
        full_url = request.form.get('url')
        short_id = request.form.get('id')
        if short_id == "":
            short_id = ''.join(random.choices(string.ascii_letters + string.digits, k=random.randint(1, 10)))

        with open(file, "r") as f:
            short_urls = json.load(f)

        short_urls[short_id] = full_url
        with open(file, "w") as f:
            json.dump(short_urls, f)

        return redirect(url_for('panel'))
    else:
        return render_template('form.html')

@url.route('/go/<short_id>')
def go(short_id):
    with open(file, "r") as f:
        short_urls = json.load(f)
    full_url = short_urls.get(short_id)
    return redirect(full_url)
@url.route('/url.json')
def serving_css():
    response = send_file('templates/url.json', mimetype='application/json')
    response.headers['Content-Type'] = 'application/json'
    return response
@url.route('/panel')
def panel():
    with open(file, "r") as f:
        short_urls = json.load(f)
    return render_template('panel.html', short_urls=short_urls)

if __name__ == '__main__':
    url.run()
