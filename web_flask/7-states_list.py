#!/usr/bin/python3
""" a script that starts a Flask web application"""
from flask import Flask
from flask import render_template
app = Flask(__name__)


@app.teardown_appcontext
def teardown_db(exception):
    """Close current SQLAlchemy sessions"""
    storage.close()


@app.route('/states_list', strict_slashes=False)
def list_states():
    """List all state objects present in DBStorage"""
    states = sorted(storage.all(State).values(), key=lambda state: state.name)
    return render_template('7-states_list.html', states=states)


if __name__ == '__main__':
    from models import storage
    from models.state import State
    app.run(host='0.0.0.0', port=5000)
