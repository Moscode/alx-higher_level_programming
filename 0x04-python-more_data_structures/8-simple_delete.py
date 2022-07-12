#!/usr/bin/python3
"""
Function to delete key from dictionary
"""


def simple_delete(a_dictionary, key=""):
    """ Delete key from a_dictionary
        Args:
            a_dictionary (dict): where to delete key from
            key (string): what should be deleted
    """
    try:
        del a_dictionary[key]
        return a_dictionary
    except KeyError:
        return a_dictionary
