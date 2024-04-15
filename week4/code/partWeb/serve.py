from flask import Flask, send_file

app = Flask(__name__)

@app.route('/')
def home():
    return 'Home page'

@app.route('/html1')
def serving_html():
    response = send_file('search/search.html', mimetype='text/html')
    response.headers['Content-Type'] = 'text/html'
    return response
@app.route('/styles.css')
def serving_css():
    response = send_file('search/styles.css', mimetype='text/css')
    response.headers['Content-Type'] = 'text/css'
    return response
@app.route('/googleLogo.png')
def serving_googleLogo():
    response = send_file('search/googleLogo.png', mimetype='image/png')
    response.headers['Content-Type'] = 'image/png'
    return response
@app.route('/search.png')
def serving_search():
    response = send_file('search/search.png', mimetype='image/png')
    response.headers['Content-Type'] = 'image/png'
    return response
@app.route('/searchImages.html')
def serving_searchImages():
    response = send_file('search/searchImages.html', mimetype='text.html')
    response.headers['Content-Type'] = 'text/html'
    return response
if __name__ == '__main__':
    app.run()
