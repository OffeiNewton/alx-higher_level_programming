#!/usr/bin/python3

"""
This module contains the Square class.
"""


class Square:
    """
    This class represents a square.
    """

    def __init__(self, size=0):
        """
        Initializes a square with a given size (default is 0).
        """
        self.__size = size

        if not isinstance(size, int):
            raise TypeError("size must be an integer")

        if size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """
        Computes the area of the square.
        """
        return self.__size ** 2
