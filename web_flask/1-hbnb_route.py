#!/usr/bin/python3
"""flask script to display greeting message”"""

from flask import Flask


app = Flask(__name__)


@app.route("/", strict_slashes=False)
def index():
    """a method to return hello HBNB"""
    return "Hello HBNB!"

@app.route("/hbnb", strict_slashes=False)
def index_hbnb():
    """a function to return HBNB"""
    return "HBNB"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)