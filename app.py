import subprocess

from waitress import serve
from flask import Flask, render_template, request

app = Flask(__name__, template_folder='templates')


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/', methods=['POST'])
def submit():
    text = request.form['text']
    if text:
        try:
            output = subprocess.check_output(f'ping -c1 {text}', shell=True)
        except subprocess.CalledProcessError:
            output = None

        if output:
            result = output.decode("utf-8")
        else:
            result = 'no pong'
    else:
        result = 'please enter an address'
    return render_template('index.html', output=result)


if __name__ == '__main__':
    serve(app, host='0.0.0.0')
