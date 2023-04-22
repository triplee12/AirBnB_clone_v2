#!/usr/bin/python3
"""AirBnB web flask."""
from flask import Flask
from os import environ
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def index():
    """Entry point."""
    return "Hello HBNB!"


if __name__ == "__main__":
    environ['FLASK_APP'] = __file__
    app.run(host='0.0.0.0', port=5000)
