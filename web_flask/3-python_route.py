#!/usr/bin/python3
"""starts a Flask web application:"""

from flask import Flask  # Import Flask class

# Create a new instance of the Flask class
app = Flask(__name__)


# Define a route for the root URL
@app.route('/', strict_slashes=False)
def hello_hbnb():
    """Display "Hello HBNB!" when the root URL is requested"""
    return 'Hello HBNB!'


# Define a route for /hbnb URL
@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Display "HBNB" when the /hbnb URL is requested"""
    return 'HBNB'


# Define a route for /c/<text> URL
@app.route('/c/<text>', strict_slashes=False)
def c(text):
    """Display "C " followed by the value of text, replacing any underscores with spaces"""
    return 'C {}'.format(text.replace('_', ' '))


# Define a route for /python/<text> URL
# The default value of text is "is cool"
@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python(text):
    """Display "Python " followed by the value of text, replacing any underscores with spaces"""
    return 'Python {}'.format(text.replace('_', ' '))


# Only start the web server if this script is executed directly
# (not imported as a module)
if __name__ == '__main__':
    # Run the Flask application
    app.run(host='0.0.0.0', port=5000)
