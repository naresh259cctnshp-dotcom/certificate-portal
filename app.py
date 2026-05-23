from flask import Flask, render_template, request, send_file

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/download', methods=['POST'])
def download():

    name = request.form['name']

    filename = f"{name}.jpeg"

    return send_file(filename, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
