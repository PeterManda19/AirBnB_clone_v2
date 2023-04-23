#!/usr/bin/python3
"""Starts a Flask web application"""

from flask import Flask, render_template
from models import storage
from models.state import State
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
