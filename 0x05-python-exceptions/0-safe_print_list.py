#!/usr/bin/python3
"""
0-safe_print_list.py: Function to print x elements of a list.
"""


def safe_print_list(my_list=[], x=0):
    """
    Prints x elements of a list.

    Args:
        my_list (list): The list to print.
        x (int): The number of elements to print.

    Returns:
        int: The real number of elements printed.
    """
    try:
        count = 0
        for i in range(x):
            print(my_list[i], end="")
            count += 1
        print()
        return count
    except IndexError:
        print()
        return count


my_list = [1, 2, 3, 4, 5]
nb_print = safe_print_list(my_list, 2)
print("nb_print: {:d}".format(nb_print))
nb_print = safe_print_list(my_list, len(my_list))
print("nb_print: {:d}".format(nb_print))
nb_print = safe_print_list(my_list, len(my_list) + 2)
print("nb_print: {:d}".format(nb_print))
