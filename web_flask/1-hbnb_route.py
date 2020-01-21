#!/usr/bin/python3
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


if __name__ == '__main__':
    """Listening route and port"""
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
