#!/usr/bin/python3
"""Module to perform integer addition."""


def add_integer(a, b=98):
    """
    Adds two integers a and b.

    a and b must be integers or floats otherwise a TypeError is raised.
    Floats are cast to integers before addition.

    Args:
        a (int or float): first number
        b (int or float): second number (98 by default)

    Returns:
        int: sum of a and b

    Raises:
        TypeError: if a or b are not integers or floats

    >>> add_integer(2, 3)
    5
    >>> add_integer(2.7, 3.2)
    5
    >>> add_integer(5)
    103
    >>> add_integer(-5, 3)
    -2
    >>> add_integer("2", 3)
    Traceback (most recent call last):
    ...
    TypeError: a must be an integer
    >>> add_integer(2, "3")
    Traceback (most recent call last):
    ...
    TypeError: b must be an integer
    >>> add_integer(0, 0)
    0
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
