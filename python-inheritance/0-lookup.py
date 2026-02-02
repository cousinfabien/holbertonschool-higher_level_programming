#!/usr/bin/python3
"""This modiule defines a function that returns
the attributes and methods of an object."""


def lookup(obj):
    """Returns a list of available attributes and methods of an object."""
    return dir(obj)
