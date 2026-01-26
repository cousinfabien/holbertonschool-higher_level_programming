#!/usr/bin/python3
"""This module defines a class Square with
size validation, area calculation and square printing."""


class Square:
    """Represent a square with a validated private size attribute."""

    def __init__(self, size=0):
        """Initialize a new Square instance with size validation.

        Args:
            size (int, optional): The size of the square. Defaults to 0.
        """
        self.size = size  # Use the setter for validation

    @property
    def size(self):
        """Retrieve the size of the square.

        Returns:
            int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square with validation.

        Args:
            value (int): The new size of the square.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Calculate and return the area of the square.

        Returns:
            int: The area of the square (size squared).
        """
        return self.__size ** 2

    def my_print(self):
        """Print the square using the # character."""
        if self.__size == 0:
            print()
            return
        for _ in range(self.__size):
            print('#' * self.__size)
