from flask import Flask, request, send_file, make_response
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import qrcode
import barcode
from barcode.writer import ImageWriter
from io import BytesIO
import random
import string
from PIL import Image, ImageDraw
from captcha.image import ImageCaptcha

app = Flask(__name__)

chart_storage = BytesIO()
qr_storage = BytesIO()

@app.route('/')
def home():
    return 'Home page'

@app.route('/chart', methods=['GET', 'POST'])
def chart():
    if request.method == 'POST':
        data = request.get_json()
        labels = [item['label'] for item in data]
        values = [item['value'] for item in data]

        fig, ax = plt.subplots()
        ax.pie(values, labels=labels, autopct='%1g')
        ax.axis('equal')

        plt.savefig(chart_storage, format='png')
        plt.close(fig)

        return "chart image is generated"
    else:
        chart_storage.seek(0)
        response = send_file(chart_storage, mimetype='image/png')
        response.headers['Content-Type'] = 'image/png'
        return response

@app.route('/qr', methods=['GET', 'POST'])
def qr():
    qr_data = request.args.get('qr_data', '')
    size = int(request.args.get('size', 50))

    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=size,
        border=4,
    )
    qr.add_data(qr_data)
    qr.make(fit=True)

    img = qr.make_image()
    img.save(qr_storage, format='PNG')

    qr_storage.seek(0)
    response = make_response(qr_storage.read())
    response.headers['Content-Type'] = 'image/png'
    return response


@app.route('/barcode', methods=['GET'])
def barcode_generator():
    text = request.args.get('text')
    code128 = barcode.get_barcode_class('code128')
    barcode_img = code128(text, writer=ImageWriter())

    bar_storage = BytesIO()
    barcode_img.write(bar_storage)
    bar_storage.seek(0)
    return send_file(bar_storage, mimetype='image/png')

@app.route('/captcha')
def captcha():
    captcha_text = ''.join(random.choices(string.ascii_letters + string.digits, k=random.randint(5, 10)))
    image = ImageCaptcha()

    image.generate(captcha_text)
    captcha_storage = BytesIO()
    
    image.write(captcha_text, captcha_storage, 'PNG')
    captcha_storage.seek(0)
    response = make_response(captcha_storage.read())
    response.headers.set('Content-Type', 'image/png')
    response.headers.set('X-Nastia-Captcha-Value', captcha_text)
    return response


if __name__ == '__main__':
    app.run(port=3132)
