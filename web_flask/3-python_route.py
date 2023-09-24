#!/usr/bin/python3
# A script that starts a flsk web application
from flask import Flask

app = Flask(__name__)
app.route ('/', strict_slashes=False)

@app.route('/')
def hello_hbnb():
    return "Hello HBNB!"

@app.route('/ hbnb', strict_slashes=False)
def hbnb():
    return "HBNB"

@app.route('/c/<text>', strict_slashes=False)
def c_text():
    return "C <text>"

@app.route('/python/<text>', strict_slashes=False)
def python_text():
    return "Python <text>"
    text = text.replace('_' ' ')
if __name__ == '__main__':
    app.run (host='0.0.0.0', port=5000)
