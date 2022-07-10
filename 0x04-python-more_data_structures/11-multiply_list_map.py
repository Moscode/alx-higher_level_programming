#!/usr/bin/python3
"""
Multiply with each element of list with using for loops
"""


def multiply_list_map(my_list=[], number=0):
    """ Multiply each element of list with number
        Args:
            my_list (list): list to compute on
            number (int): number to multiply by each element
        Returns (list): multiplied by number
    """
    return list(map(lambda x: x * number, my_list))
