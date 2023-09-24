#!/usr/bin/python3
# a script that starts a Flask application
# displays a html page only if n is an integer

from flask import Flask
app = Flask(__name__)

@app.route ('/', strict_slashes=False)
def hello_hbnb():
    return "Hello HBNB!"
@app.route ('/hbnb')
def hbnb():
    return "HBNB!"

@app.route ('/c/<text>')
def c_text():
    text = text.replace('_', ' ')
    return "C {}" .format(text)

@app.route ('/python/<text>')
def python_text(text= 'is cool'):
    text = text.replace('_', ' ')
    return "Python {}" .format(text)

@app.route ('/number/<n>')
def number_text(n):
    n = str(n)
    return "{} is a number" .format(n)

@app.route ('/number_template/<n>')
def number_template(n):
    n = str(n)
    return render_templates('5-number.html', n=n)

@app.route ('/number_odd_or_even/<n>')
def number_odd_or_even(n):
    if n % 2 == 0:
        evenness = 'even'
    else:
        even = 'odd'
    return render_template('6-number_odd_or_even.html', n=n, evenness=even)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')

