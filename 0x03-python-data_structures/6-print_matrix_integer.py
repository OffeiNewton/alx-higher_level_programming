#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    """
    Print a matrix of integers
    """
    for row in matrix:
        for num in row:
            print("{:d}".format(num), end=" ")
        print()
