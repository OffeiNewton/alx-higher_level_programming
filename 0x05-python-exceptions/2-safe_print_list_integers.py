#!/usr/bin/python3
"""
2-safe_print_list_integers.py: Function to print the first x elements of a list,
                              printing only integers.
"""


def safe_print_list_integers(my_list=[], x=0):
    """
    Prints the first x elements of a list, printing only integers.

    Args:
        my_list (list): The list to print.
        x (int): The number of elements to access in my_list.

    Returns:
        int: The real number of integers printed.
    """
    try:
        count = 0
        for i in range(x):
            if isinstance(my_list[i], int):
                print("{:d}".format(my_list[i]), end="")
                count += 1
        print()
        return count
    except IndexError:
        print()
        return count


my_list = [1, 2, 3, 4, 5]
nb_print = safe_print_list_integers(my_list, 2)
print("nb_print: {:d}".format(nb_print))

my_list = [1, 2, 3, "School", 4, 5, [1, 2, 3]]
nb_print = safe_print_list_integers(my_list, len(my_list))
print("nb_print: {:d}".format(nb_print))

nb_print = safe_print_list_integers(my_list, len(my_list) + 2)
print("nb_print: {:d}".format(nb_print))
