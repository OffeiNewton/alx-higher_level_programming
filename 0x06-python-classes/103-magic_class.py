#!/usr/bin/python3

import math


class MagicClass:
    """Represents a magic class"""

    def __init__(self, radius=0):
        """Initializes a MagicClass object with radius"""
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """Computes the area of the circle"""
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """Computes the circumference of the circle"""
        return 2 * math.pi * self.__radius
