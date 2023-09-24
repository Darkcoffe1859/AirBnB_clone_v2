#!/usr/bin/python3
# A string that starts a Flask web application
# displays an HTML page only if n is a number
from flask import Flask
app = Flask(__name__)
@app.url_map.strict_slashes = False

@app.route('/')
def hello_hbnb():
    return "Hello HBNB!"


@app.route('/hbnb')
def hbnb():
    return "HBNB!"

@app.route('/text')
def c_text(text):
    text = text.replace('_', ' ' )
    return "C {}" .format(text)

@app.route('/python')
@app.route('/python/<text>')
def python_text(text= "is cool"):
    text = text.replace('_', ' ')
    return "Python {}" .format(text)

@app.route('/number/<n>')
def number_text(n):
    n = str(n)
    return "{} is a number" .format(n)

@app.route('/number/template/<n>')
def number_template(n):
    n = str(n)
    return "{} is a number" .format(n)

if __name__ == '__main__':
    app.run(host='0.0.0.0' port=5000)
