#!/usr/bin/python3
"""This module defines a class that extends the built-in list class."""


class MyList(list):
    """Represents a list that can print itself sorted."""

    def print_sorted(self):
        """Prints the list sorted in ascending order."""
        print([x for x in sorted(self)])
