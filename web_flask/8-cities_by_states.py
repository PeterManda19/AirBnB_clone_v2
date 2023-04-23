#!/usr/bin/env python3
"""Module to start a Flask web application"""

from flask import Flask, render_template, jsonify
from models import storage, State, City
from os import environ
from sqlalchemy.orm import scoped_session
import subprocess


app = Flask(__name__)

# Create all tables before running the Flask app
storage.reload()


# Define the database credentials
db_user = "root"
db_password = ""
db_name = "hbnb_dev_db"

# Define the path to the dump file
dump_file = "/path/to/7-dump.sql"

# Run the mysql command to import the dump file
subprocess.run(
    f"mysql -u {db_user} -p{db_password} {db_name} < {dump_file}",
    shell=True,
    check=True
)


@app.teardown_appcontext
def teardown_db(exception):
    """Closes the SQLAlchemy Session."""
    storage.close()


@app.route('/cities_by_states', strict_slashes=False)
def display_states_and_cities():
    """Displays a HTML page with the list of all State objects present in DBStorage sorted by name
    (A->Z) with the list of City objects linked to the State sorted by name (A->Z)."""
    states = storage.all(State).values()
    sorted_states = sorted(states, key=lambda state: state.name)
    return render_template('8-cities_by_states.html', states=sorted_states)


if __name__ == '__main__':
    host = '0.0.0.0'
    port = 5000
    app.run(host=host, port=port)
