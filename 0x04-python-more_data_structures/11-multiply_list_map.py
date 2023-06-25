#!/usr/bin/python3

def multiply_list_map(my_list=[], number=0):
    """Multiplies each value in a list by a given number using map."""
    return list(map(lambda x: x * number, my_list))
