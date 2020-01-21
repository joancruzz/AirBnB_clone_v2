#!/usr/bin/python3
import re
from flask import Flask
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route("/")
def HelloHBNB():
    return "Hello HBNB!"


@app.route("/hbnb")
def HBNB():
    return "HBNB"


@app.route("/c/<text>")
def Ctext(text):
    return "C {}".format(text.replace("_", " "))


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
