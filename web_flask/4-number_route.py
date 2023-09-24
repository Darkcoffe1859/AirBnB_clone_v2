#!/usr/bin/python3
# A script that starts a Flask web application
from flask import Flask
app = Flask(__name__)

@app.route ('/', strict_slashes=False)
def hello_hbnb():
    return "Hello HBNB"
@app.route ('/')
def hbnb():
    return "HBNB"

@app.route ('/c/<text>')
def c_text(text):
    text = text.replace('_', '')
    return "C {}".format(text)

@app.route('/python/<text>')
def python_text(text= 'is cool'):
    text = text.replace('_', ' ')
    return "python {}".format(text)

@app.route('/number/<int:n>')
def number_text(n):
    n = str(n)
    return "{} is a number".format(n)

if __name__ == ' __main__':
    app.run(host='0.0.0.0', port=5000)
