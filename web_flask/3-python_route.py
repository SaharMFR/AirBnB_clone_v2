#!/usr/bin/python3
"""
Starts a Flask web application listening on `0.0.0.0`, port `5000`.
Routes:
    `/`: display `Hello HBNB!`.
    `/hbnb`: display `HBNB`.
    `/c/<text>`: display `C `, followed by the value of the `text`
        variable (replacing underscore `_` symbols with spaces.
    `/python/<text>`: display `Python `, followed by the value of
        the `text` variable (replacing underscore `_` symbols with
        spaces. The default value is `is cool`.
"""

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """ Returns `Hello HBNB!` """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ Returns `HBNB` """
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """
    Returns a string consists of `C `, followed by the value of the
    `text` variable (replacing underscore `_` symbols with spaces.
    """
    return 'C {}'.format(text.replace('_', ' '))


@app.route('/python/<text>', strict_slashes=False)
@app.route('/python', strict_slashes=False)
def python_text(text='is cool'):
    """
    Returns a string consists of `Python `, followed by the value of
    the `text` variable (replacing underscore `_` symbols with
    spaces. The default value is `is cool`.
    """
    return 'Python {}'.format(text.replace('_', ' '))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
