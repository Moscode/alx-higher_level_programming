#!/usr/bin/python3
"""
Function to square values in matrix
"""


def square_matrix_simple(matrix=[]):
    """Square each element of a matrix
        Args:
            matrix (list[list]): matrix to compute on
    """
    new_matrix = []
    for subMatrix in matrix:
        new_matrix.append(list(map(lambda x: x ** 2, subMatrix)))
    return new_matrix
