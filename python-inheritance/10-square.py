#!/usr/bin/python3
"""This module defines a Square class
that inherits from Rectangle."""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Represents a square defined by its size"""

    def __init__(self, size):
        """Initializes a square with a validated size."""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """Returns the area of the square."""
        return self.__size * self.__size

