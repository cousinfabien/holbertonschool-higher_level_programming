#!/usr/bin/python3
"""This module defines a base geometry class
with an unimplemented area method."""


class BaseGeometry:
    """Represents a base geometry class."""

    def area(self):
        """Raises an Exception indicating that area() is not implemented."""
        raise Exception("area() is not implemented")
