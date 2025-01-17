#!/usr/bin/python3
"""
Starts a Flask web application
"""

from flask import Flask

app = Flask(__name__) # Creates an instance of the Flask class


@app.route("/", strict_slashes=False) # Defines the root route and disables strict slashes
def hello_hbnb():
    """Displays 'Hello HBNB!'"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False) # Defines the '/hbnb' route and disables strict slashes
def hbnb():
    """Displays 'HBNB'"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False) # Defines the '/c/<text>' route and disables strict slashes
def c(text):
    """Displays 'C' followed by the value of the text variable"""
    return "C {}".format(text.replace('_', ' ')) # Replaces underscores with spaces and returns the modified string


@app.route("/python/", defaults={"text": "is cool"}, strict_slashes=False) # Defines the '/python/' route and disables strict slashes. Sets default value of 'text' to 'is cool'
@app.route("/python/<text>", strict_slashes=False) # Defines the '/python/<text>' route and disables strict slashes
def python(text):
    """Displays 'Python' followed by the value of the text variable"""
    return "Python {}".format(text.replace('_', ' ')) # Replaces underscores with spaces and returns the modified string


@app.route("/number/<int:n>", strict_slashes=False) # Defines the '/number/<n>' route and disables strict slashes. Specifies that 'n' should be an integer
def number(n):
    """Displays 'n is a number' only if n is an integer"""
    return "{} is a number".format(n) # Returns the value of 'n' as a string with the message "n is a number"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000") # Runs the app and listens on 0.0.0.0, port 5000
