#!/usr/bin/python3
"""
5-raise_exception.py: Function to raise a type exception.
"""


def raise_exception():
    """
    Raises a type exception.
    """
    raise TypeError


try:
    raise_exception()
except TypeError as te:
    print("Exception raised")
