#!/usr/bin/python3
""" Write a script that starts a Flask web application: """
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
        return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
        return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def cisfun(text):
        return "C {}".format(text.replace("_", " "))


@app.route("/python", defaults={'text': "is_cool"}, strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def pythonrun(text):
        return "Python {}".format(text.replace("_", " "))


@app.route("/number/<int:n>", strict_slashes=False)
def numN(n):
        return "{} is a number".format(n)


@app.route("/number_template/<int:n>", strict_slashes=False)
def n_template(n):
        return render_template("5-number.html", n=n)


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def number_odd_or_even(n):
        doc = "6-number_odd_or_even.html"
        if (n % 2 == 0):
                return render_template(doc, n=n, number="even")
        return render_template(doc, n=n, number="odd")

if __name__ == "__main__":
        app.run(host='0.0.0.0', port=5000)