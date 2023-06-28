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

    @property
    def size(self):
        """
        Getter method for size.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter method for size.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")

        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    def my_print(self):
        """
        Prints the square using the '#' character.
        """
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__size):
                print("#" * self.__size)
