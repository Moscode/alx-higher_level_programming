#!/usr/bin/python3
"""
Calculate weighted average using set in list
"""


def weight_average(my_list=[]):
    """ Cal weighted average
        Args:
            my_list (list): list to use for computing
        Returns (float, integer): weighted averaged
    """
    if len(my_list) == 0:
        return 0
    sum_of_val = 0
    multiple_of_val = 0
    sum_of_weight = 0
    for val_1, val_2 in my_list:
        multiple_of_val = val_1 * val_2
        sum_of_val += multiple_of_val
        sum_of_weight += val_2
    solution = sum_of_val / sum_of_weight
    return solution
