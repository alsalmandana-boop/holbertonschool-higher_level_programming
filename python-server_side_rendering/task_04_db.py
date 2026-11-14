
#!/usr/bin/python3
"""Display products from JSON, CSV, or SQLite using Flask."""

import csv
import json
import os
import sqlite3

from flask import Flask, render_template, request

app = Flask(__name__)


def read_json_file(filename):
    """Read product records from a JSON file."""
    with open(filename, 'r', encoding='utf-8') as file:
        return json.load(file)


def read_csv_file(filename):
    """Read product records from a CSV file."""
    products = []

    with open(filename, 'r', encoding='utf-8', newline='') as file:
        reader = csv.DictReader(file)

        for row in reader:
            row['id'] = int(row['id'])
            row['price'] = float(row['price'])
            products.append(row)

    return products


def read_sql_file(filename):
    """Read product records from a SQLite database."""
    conn = sqlite3.connect(filename)

    try:
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        cursor.execute(
            'SELECT id, name, category, price FROM Products'
        )
        return [dict(row) for row in cursor.fetchall()]
    finally:
        conn.close()


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


@app.route('/products')
def products():
    """Display products from the selected data source."""
    source = request.args.get('source')
    product_id = request.args.get('id')

    if source not in ('json', 'csv', 'sql'):
        return render_template(
            'product_display.html',
            products=[],
            error='Wrong source'
        )

    try:
        if source == 'json':
            path = os.path.join(app.root_path, 'products.json')
            product_list = read_json_file(path)
        elif source == 'csv':
            path = os.path.join(app.root_path, 'products.csv')
            product_list = read_csv_file(path)
        else:
            path = os.path.join(app.root_path, 'products.db')
            product_list = read_sql_file(path)

    except (OSError, ValueError, sqlite3.Error,
            json.JSONDecodeError) as error:
        return render_template(
            'product_display.html',
            products=[],
            error='Error reading products: {}'.format(error)
        )

    if product_id is not None:
        try:
            selected_id = int(product_id)
            product_list = [
                product for product in product_list
                if int(product['id']) == selected_id
            ]
        except (ValueError, TypeError, KeyError):
            product_list = []

        if not product_list:
            return render_template(
                'product_display.html',
                products=[],
                error='Product not found'
            )

    return render_template(
        'product_display.html',
        products=product_list,
        error=None
    )


if __name__ == '__main__':
    app.run(debug=True, port=5000)
