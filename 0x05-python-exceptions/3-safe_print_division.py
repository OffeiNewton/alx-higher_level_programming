#!/usr/bin/python3
"""
3-safe_print_division.py: Function to divide 2 integers and print the result.
"""


def safe_print_division(a, b):
    """
    Divides 2 integers and prints the result.

    Args:
        a (int): The dividend.
        b (int): The divisor.

    Returns:
        float: The result of the division, or None if b is 0.
    """
    try:
        result = a / b
    except ZeroDivisionError:
        result = None
    finally:
        print("Inside result: {}".format(result))
        return result


a = 12
b = 2
result = safe_print_division(a, b)
print("{:d} / {:d} = {}".format(a, b, result))

a = 12
b = 0
result = safe_print_division(a, b)
print("{:d} / {:d} = {}".format(a, b, result))
