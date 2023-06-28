#!/usr/bin/python3
"""
1-safe_print_integer.py: Function to print an integer with "{:d}".format().
"""


def safe_print_integer(value):
    """
    Prints an integer with "{:d}".format().

    Args:
        value: The value to print.

    Returns:
        bool: True if value is an integer and has been printed correctly,
              False otherwise.
    """
    try:
        print("{:d}".format(value))
        return True
    except (ValueError, TypeError):
        return False


value = 89
has_been_print = safe_print_integer(value)
if not has_been_print:
    print("{} is not an integer".format(value))

value = -89
has_been_print = safe_print_integer(value)
if not has_been_print:
    print("{} is not an integer".format(value))

value = "School"
has_been_print = safe_print_integer(value)
if not has_been_print:
    print("{} is not an integer".format(value))
