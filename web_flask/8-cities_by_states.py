#!/usr/bin/python3
"""
Starts a Flask web application.
"""
from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City

app = Flask(__name__)


@app.teardown_appcontext
def close_storage(exception):
    """
    Closes the current SQLAlchemy session.
    """
    storage.close()


@app.route('/cities_by_states', strict_slashes=False)
def display_cities_by_states():
    """
    Displays a HTML page with a list of all State
    objects and their associated City objects.
    """
    states = sorted(storage.all(State).values(), key=lambda state: state.name)
    return render_template('8-cities_by_states.html', states=states)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
