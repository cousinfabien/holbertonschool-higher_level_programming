#!/usr/bin/python3
"""Defines a counted iterator that tracks how many items have been iterated."""

class CountedIterator:
    """Iterator wrapper that counts the number of items fetched."""

    def __init__(self, iterable):
        """Initialize the iterator and counter."""
        self.iterator = iter(iterable)  # l'itérateur original
        self.count = 0                  # compteur d'éléments

    def __next__(self):
        """Return the next item and increment the counter."""
        try:
            item = next(self.iterator)  # obtient l'élément suivant
            self.count += 1             # incrémente le compteur
            return item                 # retourne l'élément
        except StopIteration:
            raise                     # relance StopIteration si fin de l'itérable

    def get_count(self):
        """Return the number of items that have been iterated."""
        return self.count
