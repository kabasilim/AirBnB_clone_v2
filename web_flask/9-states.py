#!/usr/bin/python3
"""Script that starts a Flask web application."""

from flask import Flask
from flask import render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route('/states', strict_slashes=False)
def states_list():
    """Display a HTML page with a list of all states."""
    states = storage.all(State).values()
    sorted_states = sorted(states, key=lambda state: state.name)
    return render_template('7-states_list.html', states=sorted_states)


@app.route('/states/<string:id>', strict_slashes=False)
def states_cities(id):
    """Display a HTML page with the cities of a specific state."""
    states = storage.all(State).values()
    for state in states:
        if state.id == id:
            return render_template('9-states.html', state=state)
    return render_template('9-states.html', state=None)


@app.teardown_appcontext
def teardown_db(exception):
    """Remove the current SQLAlchemy Session."""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

