#!/usr/bin/python3
"""Serialize and deserialize
custom Python objects using pickle."""


import pickle


class CustomObject:
    """Custom object with name, age, and is_student attributes."""
    def __init__(self, name, age, is_student):
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Print the object's attributes in the requested format."""
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """Serialize the current instance and save it to a file."""
        try:
            with open(filename, "wb") as f:
                pickle.dump(self, f)
        except Exception:
            pass

    @classmethod
    def deserialize(cls, filename):
        """Load and return an instance from a pickle file."""
        try:
            with open(filename, "rb") as f:
                obj = pickle.load(f)
                return obj
        except Exception:
            return None
