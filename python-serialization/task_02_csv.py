#!/usr/bin/env python3
"""Module for converting CSV data to JSON."""

import csv
import json


def convert_csv_to_json(csv_filename):
    """Convert a CSV file to JSON and return True on success."""
    try:
        with open(csv_filename, "r", encoding="utf-8") as file:
            data = list(csv.DictReader(file))

        with open("data.json", "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)

        return True

    except (OSError, csv.Error):
        return False
