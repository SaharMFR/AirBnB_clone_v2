#!/usr/bin/python3
"""
Starts a Flask web application listening on `0.0.0.0`, port `5000`.
Uses `storage` for fetching data from the storage engine.
"""
from flask import Flask, render_template
from models import storage

app = Flask(__name__)


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """Returns rendered template `100-hbnb.html`"""
    s = storage.all("State")
    a = storage.all("Amenity")
    p = storage.all("Place")
    return render_template('100-hbnb.html', states=s, amenities=a, places=p)


@app.teardown_appcontext
def teardown(self):
    """Removes the current SQLAlchemy Session"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
