#!/usr/bin/python3
"""Flask application that displays items from a JSON file."""

import json
import os
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    """Render the home page."""
    return render_template('index.html')


@app.route('/about')
def about():
    """Render the about page."""
    return render_template('about.html')


@app.route('/contact')
def contact():
    """Render the contact page."""
    return render_template('contact.html')


@app.route('/items')
def items():
    """Read items from JSON and render the items page."""
    json_path = os.path.join(app.root_path, 'items.json')

    with open(json_path, 'r', encoding='utf-8') as file:
        data = json.load(file)

    item_list = data.get('items', [])

    return render_template('items.html', items=item_list)


if __name__ == '__main__':
    app.run(debug=True, port=5000)

