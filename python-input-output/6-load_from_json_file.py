#!/usr/bin/python3
"""This module provides a function to create
a Python object to a file in JSON format."""


import json


def load_to_json_file(filename):
    """Creates a Python object to a text file using its JSON representation."""
    with open(filename, "r", encoding="utf-8") as f:
        json.load(f)
