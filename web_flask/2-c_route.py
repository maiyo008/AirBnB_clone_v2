#!/usr/bin/python3
""" a script that starts a Flask web application"""
from flask import Flask
from werkzeug.utils import escape
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """Display 'Hello HBNB!'"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Display "HBNB" """
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_is_fun(text):
    """Display argument passed as text.
    Replace underscore with space
    """
    text = text.replace('_', ' ')
    return 'C %s' % escape(text)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
