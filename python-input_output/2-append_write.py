#!/usr/bin/python3
"""This module provides a function to
append a string to a text file."""


def append_write(filename="", text=""):
    """Appends a string to a UTF8 text file and
    returns the number of characters written."""
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
