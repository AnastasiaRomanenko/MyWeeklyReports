from flask import Flask, request, redirect, jsonify
import json
import random
import string

app = Flask(__name__)

file = "templates/url.json"

@app.route('/')
def home():
    return 'Home page'

@app.route('/shorten', methods=['POST', 'GET'])
def shorten():
        full_url = request.args.get('url')
        short_id = request.args.get('id', ''.join(random.choices(string.ascii_letters + string.digits, k=random.randint(1, 10))))

        with open(file, "r") as f:
            short_urls = json.load(f)

        short_urls[short_id] = full_url
        with open(file, "w") as f:
            json.dump(short_urls, f)

        short_url = f"localhost:3132/go/{short_id}"
        return jsonify({"short_url": short_url})

@app.route('/go/<short_id>')
def go(short_id):
    with open(file, "r") as f:
        short_urls = json.load(f)
    full_url = short_urls.get(short_id)
    return redirect(full_url)

if __name__ == '__main__':
    app.run(port=3132)