#!/usr/bin/env python3
"""Serialize and deserialize custom Python objects."""

import pickle


class CustomObject:
    """Represent a custom object."""

    def __init__(self, name, age, is_student):
        """Initialize the object."""
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Display object attributes."""
        print("Name: {}".format(self.name))
        print("Age: {}".format(self.age))
        print("Is Student: {}".format(self.is_student))

    def serialize(self, filename):
        """Serialize the object to a file."""
        try:
            with open(filename, "wb") as file:
                pickle.dump(self, file)
        except (OSError, pickle.PickleError):
            return None

    @classmethod
    def deserialize(cls, filename):
        """Deserialize an object from a file."""
        try:
            with open(filename, "rb") as file:
                obj = pickle.load(file)
            if not isinstance(obj, cls):
                return None
            return obj
        except (OSError, pickle.UnpicklingError, EOFError,
                AttributeError, ImportError):
            return None
