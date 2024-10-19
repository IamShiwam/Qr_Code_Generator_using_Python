from flask import Flask, render_template, request, send_file
import qrcode

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate_qr():
    data = request.form.get('data')  # Get data from the form

    # Create a QR code
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4
    )
    qr.add_data(data)
    qr.make(fit=True)

    # Generate and save the QR code
    img = qr.make_image(fill_color="black", back_color="white")
    img.save("static/qr_code.png")  # Save the image in the static folder

    return render_template('index.html', qr_code_image="static/qr_code.png")

if __name__ == '__main__':
    app.run(debug=True)
