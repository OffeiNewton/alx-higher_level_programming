#!/usr/bin/python3

class Square:
    """Defines a square"""

    def __init__(self, size=0):
        """Instantiates a Square object with size"""
        self.size = size

    @property
    def size(self):
        """Retrieves the size of the square"""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the size of the square"""
        if not isinstance(value, (int, float)):
            raise TypeError("size must be a number")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Returns the current square area"""
        return self.__size ** 2

    def __lt__(self, other):
        """Less than comparison"""
        return self.area() < other.area()

    def __le__(self, other):
        """Less than or equal comparison"""
        return self.area() <= other.area()

    def __eq__(self, other):
        """Equal comparison"""
        return self.area() == other.area()

    def __ne__(self, other):
        """Not equal comparison"""
        return self.area() != other.area()

    def __gt__(self, other):
        """Greater than comparison"""
        return self.area() > other.area()

    def __ge__(self, other):
        """Greater than or equal comparison"""
        return self.area() >= other.area()
