from flask import Flask, render_template, request, send_file

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/download', methods=['POST'])
def download():

    name = request.form.get('name')

    filename = f"{name}.jpeg"

    return send_file(
        filename,
        as_attachment=True,
        download_name=f"{name}_certificate.jpeg"
    )

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
