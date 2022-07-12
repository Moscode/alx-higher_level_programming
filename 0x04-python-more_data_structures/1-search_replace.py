#!/usr/bin/python3
"""
Function for replacing certain element in a list
"""


def search_replace(my_list, search, replace):
    """ Function to search and replace with new list
        Args:
            my_list (list): list to search
            search (any type): value to search for
            replace (any type): value to replace with
    """
    new_list = []
    for i, val in enumerate(my_list):
        if val == search:
            new_list.append(replace)
        else:
            new_list.append(val)
    return new_list
