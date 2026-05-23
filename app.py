from flask import Flask, render_template, send_file, request
import os

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/download', methods=['POST'])
def download():

    name = request.form['name']

    file_path = "Naresh.jpeg"

    return send_file(
        file_path,
        as_attachment=True,
        download_name=f"{name}_certificate.jpg"
    )

if __name__ == '__main__':
    app.run(debug=True)
