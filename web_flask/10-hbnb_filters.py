#!/usr/bin/python3
"""
Starts a Flask web application listening on `0.0.0.0`, port `5000`.
Uses `storage` for fetching data from the storage engine.
"""
from flask import Flask, render_template
from models import storage

app = Flask(__name__)


@app.route("/hbnb_filters", strict_slashes=False)
def hbnb_filters():
    """Returns rendered template `10-hbnb_filters.html`"""
    s = storage.all("State")
    a = storage.all("Amenity")
    return render_template('10-hbnb_filters.html', states=s, amenities=a)


@app.teardown_appcontext
def teardown(self):
    """Removes the current SQLAlchemy Session"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
