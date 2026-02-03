#!/usr/bin/python3
"""Abstract Animal class with Dog and Cat subclasses."""


from abc import ABC, abstractmethod


class Animal(ABC):
    """Abstract base class representing an animal."""

    @abstractmethod
    def sound(self):
        """Abstract method to be implemented by subclasses."""
        pass


class Dog(Animal):
    """Dog class, subclass of Animal"""

    def sound(self):
        """Returns the sound of a dog"""
        return "Bark"


class Cat(Animal):
    """Cat class, subclass of Animal"""

    def sound(self):
        """Returns the sound of a cat"""
        return "Meow"
