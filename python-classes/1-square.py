#!/usr/bin/python3
"""This module defines a class Square with a private size attribute."""


class Square:
    """Represent a square with a private size attribute."""
    def __init__(self, size):
        """Initialize a new Square instance.
        Args:
            size (any type): Size of square.
        """
        self.__size = size
