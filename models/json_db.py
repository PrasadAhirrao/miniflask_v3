"""
dal.py
--------
Implements the model for our website by simulating a database.

Note: although this is nice as a simple example, don't do this in a real-world
production setting. Having a global object for application data is asking for
trouble.
"""

import json


def load_db():
    with open(
        "C:\\Users\Admin\\PycharmProjects\\miniflask_v3\\models\\flaskcard_db.json"
    ) as f:
        return json.load(f)


db = load_db()