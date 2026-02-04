#!/usr/bin/python3
"""Defines a list subclass that
prints messages when modified."""


class VerboseList(list):
    """List subclass that prints notifications when items are
    added or removed"""

    def append(self, item):
        """Add an item to the list and print a message"""
        super().append(item)
        print(f"Added [{item}] to the list.")

    def extend(self, iterable):
        """Extends the list with multiple items and print a message"""
        count = len(iterable)
        super().extend(iterable)
        print(f"Extended the list with [{count}] items.")

    def remove(self, item):
        """Remove an item from the list and print a message"""
        print(f"Removed [{item}] from the list.")
        super().remove(item)

    def pop(self, index=-1):
        """Remove and return an item from the list, printing a message"""
        item = self[index]
        print(f"Popped [{item}] from the list.")
        return super().pop(index)
