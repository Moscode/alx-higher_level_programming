#!/usr/bin/python3
"""
Update Dictionary
"""


def update_dictionary(a_dictionary, key, value):
    """ Function for creating element of a dictionary or update it if exit
        Args:
            a_dictionary (dict): what to update
            key (string): key to set
            value (any type): value to set
    """
    for i in range(len(a_dictionary)):
        a_dictionary[key] = value
    return a_dictionary
