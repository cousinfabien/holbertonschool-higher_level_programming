#!/usr/bin/python3
"""This module defines a Student class with
JSON serialization and optional attribute filtering."""


class Student:
    """Represents a student with first name, last name, and age."""

    def __init__(self, first_name, last_name, age):
        """Initialize a Student instance."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Returns a dictionary representation of the Student instance.
        If attrs is a list of strings,
        only attributes in this list are included.
        Otherwise, all attributes are returned.
        """
        if isinstance(attrs, list) and all(isinstance(a, str) for a in attrs):
            return {a: getattr(self, a) for a in attrs if hasattr(self, a)}
        return self.__dict__.copy()

    def reload_from_json(self, json):
        """
        Replaces all attributes of the Student
        instance with values from a dictionary.
        json: dictionary where key = attribute name, value = attribute value
        """
        for key, value in json.items():
            setattr(self, key, value)
