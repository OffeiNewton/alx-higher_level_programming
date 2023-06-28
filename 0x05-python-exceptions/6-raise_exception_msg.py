#!/usr/bin/python3
"""
6-raise_exception_msg.py: Function to raise a name exception with a message.
"""


def raise_exception_msg(message=""):
    """
    Raises a name exception with a message.

    Args:
        message (str): The message for the exception.
    """
    raise NameError(message)


try:
    raise_exception_msg("C is fun")
except NameError as ne:
    print(ne)
