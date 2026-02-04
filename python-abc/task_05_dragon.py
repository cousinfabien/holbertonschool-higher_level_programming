#!/usr/bin/python3
"""Demonstrates the use of mixins to add behavior to a class."""

class SwimMixin:
    """Mixin class that adds swimming capability."""

    def swim(self):
        """Print a swimming message."""
        print("The creature swims!")

class FlyMixin:
    """Mixin class that adds flying capability."""

    def fly(self):
        """Print a flying message."""
        print("The creature flies!")

class Dragon(SwimMixin, FlyMixin):
    """A dragon that can both swim and fly."""

    def roar(self):
        """Print a roaring message."""
        print("The dragon roars!")
