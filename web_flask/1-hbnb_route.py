#!/usr/bin/python3
"""WebFlask module"""
from flask import Flask
from os import environ
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_route():
    """Display Hello HBNB"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb_route():
    """Display HBNB"""
    return 'HBNB'


if __name__ == '__main__':
    environ['FLASK_APP'] = __file__
    app.run(host='0.0.0.0', port=5000)
