#!/usr/bin/python3
"""Flask web application"""
import re
from flask import Flask
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def HelloHBNB():
    "Route to display text"
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def HBNB():
    "Route to display text"
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def CText(text):
    "Route to display text"
    return "C {}".format(text.replace("_", " "))


if __name__ == '__main__':
    """Listening route and port"""
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
