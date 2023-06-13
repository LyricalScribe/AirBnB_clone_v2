#!/usr/bin/python3
"""App instance of a Flash Web App"""

from models import storage
from models.state import State
from os import environ
from flask import Flask, render_template

app = Flask(__name__)


@app.teardown_appcontext
def clean_up(exception=None):
    """Removes current SQLAlchemy session"""
    storage.close()


@app.route('/states_list', strict_slashes=False)
def states_list():
    """Displays a list of all states"""
    states = storage.all(State)
    return render_template('8-states_list.html', states=states)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
