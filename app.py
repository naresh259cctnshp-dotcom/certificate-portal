
from flask import Flask, render_template, request, send_from_directory
import os

app = Flask(__name__)

CERTIFICATE_FOLDER = 'certificates'

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/download', methods=['POST'])
def download():
    name = request.form['name'].strip()

    extensions = ['.pdf', '.jpg', '.jpeg', '.png']

    for ext in extensions:
        filename = f"{name}{ext}"
        file_path = os.path.join(CERTIFICATE_FOLDER, filename)

        if os.path.exists(file_path):
            return send_from_directory(
                CERTIFICATE_FOLDER,
                filename,
                as_attachment=True
            )

    return f"Certificate for '{name}' not found"

@app.route('/health')
def health():
    return "Server Running Successfully"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
