#!/usr/bin/python3
"""This module defines a Student class with JSON serialization support."""


class Student:
    """Represents a student with first name, last name, and age."""

    def __init__(self, first_name, last_name, age):
        """Initialize a Student instance."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        Returns a dictionary representation of the Student instance
        with only simple data structures (for JSON serialization).
        """
        return self.__dict__.copy()
