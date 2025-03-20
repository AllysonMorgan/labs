from flask import Flask, render_template,request
import segno
import os

app = Flask(__name__)

os.makedirs('static/qr_codes', exist_ok=True)

@app.route('/', methods=['GET', 'POST'])

def index():
    qr_code_filename = None
    message = None
    if request.method == 'POST':
        message = request.form['data']
        if message:
            qr_code_filename = f'static/qrcodes/qr_code.png'
            qr = segno.make(message)
            qr.save(qr_code_filename, scale=4)
    return render_template('index.html', message=message, qr_code_filename=qr_code_filename)

if __name__ == '__main__':
    app.run(debug=True)