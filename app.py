from flask import Flask, render_template, send_file, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/download', methods=['POST'])
def download():

    name = request.form.get('name')

    return send_file(
        'Naresh.jpeg',
        as_attachment=True,
        download_name=f"{name}_certificate.jpg"
    )

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
