#!/usr/bin/python3
"""
Starts a Flask web application
"""

from flask import Flask

# Create a new Flask application instance
app = Flask(__name__)


# Define a route for the root URL path '/'
# Set strict_slashes=False to allow for URLs with or without a trailing slash
@app.route('/', strict_slashes=False)
def hello():
    """
    Displays 'Hello HBNB!' when the root URL is accessed
    """
    return 'Hello HBNB!'


# Define a route for the '/hbnb' URL path
# Set strict_slashes=False to allow for URLs with or without a trailing slash
@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
    Displays 'HBNB' when the '/hbnb' URL is accessed
    """
    return 'HBNB'


# Define a route for the '/c/<text>' URL path
# Set strict_slashes=False to allow for URLs with or without a trailing slash
@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """
    Displays 'C ' followed by the value of the text variable (replace underscore _ symbols with a space)
    when the '/c/<text>' URL is accessed
    """
    return 'C {}'.format(text.replace('_', ' '))


# Start the Flask application, listening on host '0.0.0.0' and port 5000
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
