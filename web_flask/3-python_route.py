#!/usr/bin/python3
"""script that starts a Flask web application"""
from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """displays “Hello HBNB!” on route /"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """displays “HBNB” on route /hbnb"""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def C_isfun(text):
    """display C followed by the value of the text variable"""
    return f"C {text.replace('_', ' ')}"


@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_isfun(text="is cool"):
    """display Python followed by the value of the text variable"""
    return f"Python {text.replace('_', ' ')}"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
