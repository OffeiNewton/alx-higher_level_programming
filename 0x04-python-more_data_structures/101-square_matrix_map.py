#!/usr/bin/python3

def square_matrix_map(matrix=[]):
    """
    Computes the square value of all integers in a matrix using map.

    Args:
        matrix (list): 2-dimensional array representing the matrix.

    Returns:
        list: New matrix with each value squared.
    """
    return list(map(lambda row: list(map(lambda x: x ** 2, row)), matrix))
