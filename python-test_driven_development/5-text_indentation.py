#!/usr/bin/python3
"""
Module to print text with 2 new lines after '.', '?', and ':'.
"""


def text_indentation(text):
    """
    Prints a text with 2 new lines after each '.', '?', and ':'.

    Args:
        text (str): text to be indented

    Raises:
        TypeError: if text is not a string
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    delimiters = ".?:"
    start = 0
    n = len(text)

    for i, char in enumerate(text):
        if char in delimiters:
            segment = text[start:i + 1].strip()
            if segment:
                # Pour tous les segments sauf le dernier, on ajoute 2 sauts de ligne
                print(segment, end="\n\n")
            start = i + 1

    # Segment restant après le dernier délimiteur
    remaining = text[start:].strip()
    if remaining:
        print(remaining, end="")
