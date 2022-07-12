#!/usr/bin/python3
"""
Function to sort dictionary using keys
"""


def print_sorted_dictionary(a_dictionary):
    """ Function for dictionary sorting
        Args:
            a_dictionary (dictionary): dictionary to sort
        Returns (dictionary): sorted
    """
    key_list = list(a_dictionary)
    value_list = []
    sorted_key = sorted(key_list)
    for key in sorted_key:
        value_list.append(a_dictionary[key])
    for i in range(len(sorted_key)):
        print("{}: {}".format(sorted_key[i], value_list[i]))
