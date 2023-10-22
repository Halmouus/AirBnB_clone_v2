#!/usr/bin/python3
"""script that starts a Flask web application"""
from flask import Flask, render_template, app
from models import storage
from models.state import State
from models.city import City

app = Flask(__name__)


@app.route("/states_list", strict_slashes=False)
def states_list():
    """Display a list of states and their cities"""
    states = list(storage.all(State).values())
    states.sort(key=lambda x: x.name)
    return render_template('7-states_list.html', states=states)


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    """Display a list of states and their cities"""
    states = list(storage.all("State").values())
    states.sort(key=lambda x: x.name)
    return render_template('8-cities_by_states.html', states=states)


@app.teardown_appcontext
def close_storage(exception):
    """Remove the current SQLAlchemy session"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
