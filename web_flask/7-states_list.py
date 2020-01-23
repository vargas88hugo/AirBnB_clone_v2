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


@app.route('/states_list', strict_slashes=False)
def states_list():
    states = list(storage.all("State").values())
    states.sort(key=lambda state: state.name)
    return render_template('7-states_list.html', states=states)


if __name__ == '__main__':
    app.run("0.0.0.0", 5000)
