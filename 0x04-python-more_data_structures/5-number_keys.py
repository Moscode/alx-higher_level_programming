#!/usr/bin/python3
"""
Function to determine number of keys
"""


def number_keys(a_dictionary):
    """ Number of keys in dictionary
        Args:
            a_dictionary (dictionary): dict to check
        Returns total (int): number of keys
    """
    key_list = list(a_dictionary)
    total = 0
    for i in range(len(key_list)):
        total += 1
    return total
