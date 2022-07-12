#!/usr/bin/python3
"""

"""


def pascal_triangle(n):
    row = []
    matrix = []
    if n <= 0:
        return [n]
    if n == 1:
        row.append(n)
        matrix.append(row)
        return matrix
    if n == 2:
        row.append(1)
        row.append(1)
        matrix.append(row)
        return matrix
    
