#!/usr/bin/python3
"""This module provides a function to convert a class
object to a JSON-serializable dictionary."""


def class_to_json(obj):
    """
    Returns the dictionary description of a class instance with simple
    data structures (list, dict, str, int, bool) for JSON serialization.
    """
    return obj.__dict__.copy()
