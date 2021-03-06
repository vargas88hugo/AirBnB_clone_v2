#!/usr/bin/python3
"""
This script starts a Flask web application printing Hello World
and include route /hbnb, also add a variable rule with c and python
"""
from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_world():
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return "HBNB"


# <> variable rules by marking section of the url
@app.route('/c/<text>', strict_slashes=False)
def c(text):
    return "C %s" % text.replace("_", " ")


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python(text='is_cool'):
    return "Python %s" % text.replace("_", " ")


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
