#!/usr/bin/python3
"""Starts a Flask web application"""

from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.teardown_appcontext
def teardown_db(exception):
    """Removes the current SQLAlchemy session"""
    storage.close()


@app.route('/hbnb_filters', strict_slashes=False)
def hbnb_filters():
    """Displays a HTML page with a list of states and amenities"""
    states = sorted(storage.all(State).values(), key=lambda x: x.name)
    amenities = sorted(storage.all(Amenity).values(), key=lambda x: x.name)
    return render_template(
        '10-hbnb_filters.html',
        states=states,
        amenities=amenities
        )


if __name__ == '__main__':
    from models import storage
    from models.state import State
    from models.amenity import Amenity
    app.run(host='0.0.0.0', port=5000)
