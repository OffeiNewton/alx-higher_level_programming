#!/usr/bin/python3

"""
This module contains the Square class.
"""


class Square:
    """
    This class represents a square.
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes a square with a given size (default is 0) and position (default is (0, 0)).
        """
        self.__size = size
        self.__position = position

        if not isinstance(size, int):
            raise TypeError("size must be an integer")

        if size < 0:
            raise ValueError("size must be >= 0")

        if not isinstance(position, tuple) or len(position) != 2 or \
                not isinstance(position[0], int) or not isinstance(position[1], int) or \
                position[0] < 0 or position[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")

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

    @property
    def position(self):
        """
        Getter method for position.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Setter method for position.
        """
        if not isinstance(value, tuple) or len(value) != 2 or \
                not isinstance(value[0], int) or not isinstance(value[1], int) or \
                value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")

        self.__position = value

    def my_print(self):
        """
        Prints the square using the '#' character and position.
        """
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__position[1]):
                print()
            for _ in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)
