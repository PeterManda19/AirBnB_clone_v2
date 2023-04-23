#!/usr/bin/python3
"""
Flask web application that serves simple routes
"""

import os
from flask import Flask, abort, render_template

# Create a new Flask application instance
app = Flask(__name__)

# Define the routes

@app.route('/', strict_slashes=False)
def hello():
    """
    Displays "Hello HBNB!" on the root URL path '/'
    """
    return 'Hello HBNB!'

@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
    Displays "HBNB" on the '/hbnb' URL path
    """
    return 'HBNB'

@app.route('/c/<text>', strict_slashes=False)
def c_is_fun(text):
    """
    Displays "C <text>" on the '/c/<text>' URL path, with underscores
    replaced by spaces
    """
    return 'C {}'.format(text.replace('_', ' '))

# Handle 404 errors with a custom error page
@app.errorhandler(404)
def page_not_found(error):
    """
    Renders a custom 404 error page
    """
    return render_template('404.html'), 404

if __name__ == '__main__':
    # Use environment variables to set Flask app configuration
    app.config['DEBUG'] = os.getenv('FLASK_DEBUG', False)
    app.config['SECRET_KEY'] = os.getenv('FLASK_SECRET_KEY', 'dev')

    # Use a separate file for Flask app configuration
    app.config.from_pyfile('config.cfg', silent=True)

    # Use a logging library to log application activity
    import logging
    from logging.handlers import RotatingFileHandler
    handler = RotatingFileHandler('app.log', maxBytes=10000, backupCount=1)
    handler.setLevel(logging.INFO)
    app.logger.addHandler(handler)

    # Start the Flask application, listening on host '0.0.0.0' and port 5000
    app.run(host='0.0.0.0', port=5000)
