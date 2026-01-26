#!/usr/bin/python3
"""This module defines a class Square with size validation."""


class Square:
    """Represent a square with a validated private size attribute."""

    def __init__(self, size=0):
        """Initialize a new Square instance with size validation.

        Args:
            size (int, optional): The size of the square. Defaults to 0.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
