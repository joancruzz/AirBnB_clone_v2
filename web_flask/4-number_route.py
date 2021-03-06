#!/usr/bin/python3
"""Flask web application"""
import re
from flask import Flask
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


if __name__ == '__main__':
    """Listening route and port"""
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
