#!/usr/bin/python3
"""
Module that prints a text with 2 new lines after each '.', '?', and ':'.
"""


def text_indentation(text):
    """
    Prints a text with 2 new lines after each '.', '?', or ':'.

    Segments are trimmed of spaces. Consecutive delimiters are handled
    without producing extra empty lines.

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
            # take segment including delimiter
            segment = text[start:i + 1].strip()
            if segment:
                print(segment)
            start = i + 1  # move past delimiter

    # print the last segment if any
    last_segment = text[start:].strip()
    if last_segment:
        print(last_segment)
