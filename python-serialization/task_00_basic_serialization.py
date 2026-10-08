#!/usr/bin/env python3
"""Basic JSON serialization module."""

import json


def serialize_and_save_to_file(data, filename):
    """Save dictionary to JSON file."""
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(data, file)


def load_and_deserialize(filename):
    """Load JSON file and return dictionary."""
    with open(filename, "r", encoding="utf-8") as file:
        return json.load(file)
