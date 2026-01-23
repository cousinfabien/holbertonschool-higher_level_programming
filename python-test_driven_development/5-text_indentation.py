#!/usr/bin/python3
"""
Module that prints a text with a new line after each '.', '?', and ':'.
"""


def text_indentation(text):
    """
    Prints a text with a new line after each '.', '?', or ':'.

    Args:
        text (str): the text to print

    Raises:
        TypeError: if text is not a string
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    delimiters = ".?:"
    start = 0

    for i, char in enumerate(text):
        if char in delimiters:
            segment = text[start:i + 1].strip()
            if segment:
                print(segment, end="")
            start = i + 1

    last_segment = text[start:].strip()
    if last_segment:
        print(last_segment, end="")
