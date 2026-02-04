#!/usr/bin/python3
"""Demonstrates multiple inheritance with Fish and Bird classes."""

class Fish:
    """Represents a fish."""

    def swim(self):
        """Fish swimming behavior."""
        print("The fish is swimming")

    def habitat(self):
        """Fish habitat."""
        print("The fish lives in water")

class Bird:
    """Represents a bird."""

    def fly(self):
        """Bird flying behavior."""
        print("The bird is flying")

    def habitat(self):
        """Bird habitat."""
        print("The bird lives in the sky")

class FlyingFish(Fish, Bird):
    """Represents a flying fish, inherits from both Fish and Bird."""

    def fly(self):
        """Override fly behavior."""
        print("The flying fish is soaring!")

    def swim(self):
        """Override swim behavior."""
        print("The flying fish is swimming!")

    def habitat(self):
        """Override habitat behavior."""
        print("The flying fish lives both in water and the sky!")
