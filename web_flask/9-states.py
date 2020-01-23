#!/usr/bin/python3
"""
Script that routes to state_list and displays a list of states
"""
from flask import Flask
from flask import render_template
from models import storage
from models import State


app = Flask(__name__)


@app.teardown_appcontext
def closedb(foo):
    storage.close()


@app.route('/states', strict_slashes=False)
@app.route('/states/<id>', strict_slashes=False)
def states(id=None):
    state, states = None, None
    if not id:
        states = list(storage.all("State").values())
    else:
        states = storage.all("State")
        strg = "State." + id
        if strg in states:
            state = states[strg]
        else:
            state = None
        states = []
    return render_template('9-states.html', states=states, state=state, id=id)


if __name__ == '__main__':
    app.run("0.0.0.0", 5000)
