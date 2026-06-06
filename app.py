from flask import Flask, render_template, request, send_from_directory
import os

app = Flask(__name__)

CERTIFICATE_FOLDER = "certificates"

@app.route('/')
def home():
    return render_template('index.html')

# DEBUG ROUTE
@app.route('/files')
def files():
    try:
        return "<br>".join(os.listdir(CERTIFICATE_FOLDER))
    except Exception as e:
        return str(e)

@app.route('/download', methods=['POST'])
def download():

    name = request.form['name'].strip().upper()

    possible_files = [
        f"{name}.jpg",
        f"{name}.jpeg",
        f"{name}.png",
        f"{name}.pdf"
    ]

    for filename in possible_files:

        file_path = os.path.join(CERTIFICATE_FOLDER, filename)

        print("Checking:", file_path)
        print("Exists:", os.path.exists(file_path))

        if os.path.exists(file_path):

            print("FOUND:", filename)

            return send_from_directory(
                CERTIFICATE_FOLDER,
                filename,
                as_attachment=True
            )

    print("NOT FOUND:", name)

    return render_template(
        'index.html',
        error="Enter Correct Registration Number"
    )

if __name__ == '__main__':
    app.run(debug=True)
