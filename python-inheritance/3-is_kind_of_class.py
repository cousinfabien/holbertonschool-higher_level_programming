#!/usr/bin/python3
"""This module defines a function to check if
an object is an instance of or inherits from a specified class."""


def is_kind_of_class(obj, a_class):
    """Returns True if the object is an instance of,
     or inherits from, the specified class; otherwise False."""
    return isinstance(obj, a_class)
