#!/usr/bin/python3
"""
Flask framework
"""

from flask import Flask

# create a new Flask application instance
app = Flask(__name__)


# define a route for the root URL path '/'
# set strict_slashes=False to allow for URLs with or without a trailing slash
@app.route('/', strict_slashes=False)
def hello():
    """
    Displays 'Hello HBNB!' when the root URL is accessed
    """
    # return a simple string that says "Hello HBNB!"
    return 'Hello HBNB!'


# start the Flask application, listening on host '0.0.0.0' and port 5000
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
