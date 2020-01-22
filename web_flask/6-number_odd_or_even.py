#!/usr/bin/python3
"""Flask web application"""
import re
from flask import Flask, render_template
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def HelloHBNB():
    """Route to display text"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def HBNB():
    """Route to display text"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def CText(text):
    """Route to display text"""
    return "C {}".format(text.replace("_", " "))


@app.route("/python/", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def PythonText(text="is cool"):
    """Route to display text"""
    return "Python {}".format(text.replace("_", " "))


@app.route("/number/<int:n>", strict_slashes=False)
def number(n):
    """Route to display integer"""
    return "{} is a number".format(n)


@app.route("/number_template/<int:n>", strict_slashes=False)
def NumberTemplate(n):
    """Route to display html page if n is an integer"""
    return render_template('5-number.html')


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def EvenOrOdd(n):
    """Route to display html page if n is an integer"""
    if (n % 2 == 0):
        return render_template('6-number_odd_or_even.html', n=n)
    else:
        return render_template('6-number_odd_or_even.html', n=n)


if __name__ == '__main__':
    """Listening route and port"""
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
