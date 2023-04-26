#!/usr/bin/python3
"""
Starts a Flask web application that handles States and Cities objects.
"""
from flask import Flask, render_template
app = Flask(__name__)


@app.teardown_appcontext
def teardown(self):
    """
    Closes the current SQLAlchemy session.
    """
    storage.close()


@app.route('/states', strict_slashes=False)
def states():
    """
    Displays an HTML page that lists all State objects in DBStorage.
    """
    states = sorted(storage.all(State).values(), key=lambda state: state.name)
    return render_template('7-states_list.html', states=states)


@app.route('/states/<string:id>', strict_slashes=False)
def states_id(id=None):
    """
    Displays an HTML page that lists all City objects linked to a State.
    """
    return render_template('9-states.html',
                           states=storage.all(State)
                           .get('State.{}'.format(id)))


if __name__ == '__main__':
    from models import storage
    from models.state import State
    app.run(host='0.0.0.0', port='5000')
