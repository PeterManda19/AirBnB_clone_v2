#!/usr/bin/python3
"""Starts a Flask web application"""

from flask import Flask, render_template
from models import storage
from models.state import State


app = Flask(__name__)

# Create all tables before running the Flask app
storage.reload()


@app.teardown_appcontext
def teardown_appcontext(exception):
    """Removes the current SQLAlchemy session"""
    storage.close()


@app.route('/states_list', strict_slashes=False)
def states_list():
    """Displays a list of all State objects sorted by name"""
    states = sorted(storage.all(State).values(), key=lambda s: s.name)
    return render_template('7-states_list.html', states=states)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
