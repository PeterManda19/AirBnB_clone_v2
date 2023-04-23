#!/usr/bin/python3
"""Flask framework"""

from flask import Flask, render_template
app = Flask(__name__)

# define a route for the root URL path '/'
# and set strict_slashes=False to allow for URLs with or without a trailing slash
@app.route('/', strict_slashes=False)
def hello():
    """display Hello HBNB!"""
    return 'Hello HBNB!'


# define a route for '/hbnb' URL path
# and set strict_slashes=False to allow for URLs with or without a trailing slash
@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """display HBNB"""
    return 'HBNB'


# define a route for '/c/<text>' URL path
# where <text> is a variable that can be any string
# and set strict_slashes=False to allow for URLs with or without a trailing slash
@app.route('/c/<text>', strict_slashes=False)
def c(text):
    """display C followed by the text"""
    return 'C {}'.format(text.replace('_', ' '))

# start the Flask application, listening on host '0.0.0.0' and port 5000
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
