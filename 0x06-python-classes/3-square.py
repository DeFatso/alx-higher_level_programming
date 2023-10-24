#!/usr/bin/python3
"""Defines a square by size."""


class Square:

    def __init__(self, size=0):
        """Instantiates a new Square object with an optional size."""
        self.__size = size  # Set the size attribute

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """Calculates and returns the square's area."""
        return self.__size ** 2
