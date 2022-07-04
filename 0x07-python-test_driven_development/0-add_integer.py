#!/usr/bin/python3
""" Add two integers
    Args:
        a (int): first  integer, b (int): second integer
    Return:
        Sum of the two integers"""


def add_integer(a, b=98):
    """ 
    Takes two values and return their sum 
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)
    return a + b
