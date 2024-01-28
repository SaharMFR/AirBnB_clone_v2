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
    `/number/<n>`: display `(n) is a number` only if n is an integer.
    `/number_template/<n>`: display a HTML page only if `n` is an integer.
    `/number_odd_or_even/<n>`: display a HTML page only if `n` is an integer.
"""

from flask import Flask, render_template

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


@app.route('/number/<int:n>', strict_slashes=False)
def is_integer(n):
    """
    Returns a string consists of the value of `n`, followed by
    ` is a number` only if n is an integer.
    """
    return '{} is a number'.format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """
    Returns rendered template `5-number.html` only if `n` is integer.
    """
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def odd_or_even(n):
    """
    Returns rendered template `6-number_odd_or_even.html` only if
    `n` is an integer, and if it is even or odd.
    """
    if n % 2 == 0:
        return render_template('6-number_odd_or_even.html', n=n, e_or_o='even')
    return render_template('6-number_odd_or_even.html', n=n, e_or_o='odd')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
