#!/usr/bin/python3
"""
Starts a Flask web application listening on `0.0.0.0`, port `5000`.
Uses `storage` for fetching data from the storage engine.
Routes:
    `/states`: display a HTML page (list of all `State` objects
        present in `DBStorage` sorted by `name`).
    `/states/<id>`: diplay a HTML page contains the `State` with this
        `id` and a list of its cities if found, OR `Not found!`.
"""

from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route('/states', strict_slashes=False)
def states():
    """
    Returns rendered template `9-states.html` with a list
    all states sorted by `name`.
    """
    states = storage.all(State)
    return render_template('9-states.html', states=states, opt="all")


@app.route('/states/<id>', strict_slashes=False)
def state_by_id(id):
    """
    Returns rendered template `9-states.html` with info about
    the state with passed `id`.
    """
    for state in storage.all(State).values()
        if state.id == id:
            return render_template('9-states.html', states=state, opt="one")
    return render_template('9-states.html', states=state, opt="notFound")


@app.teardown_appcontext
def teardown(self):
    """Removes the current SQLAlchemy Session"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
