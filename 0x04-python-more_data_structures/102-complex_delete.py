#!/usr/bin/python3
"""
Delete items from dictionary using value to search
"""


def complex_delete(a_dictionary, value):
    """ Deleting an item from diction based on value
        Args:
            a_dictionary (dict): where to delete from
            value (any): check for value
        Returns (dict): new value
    """
    key_list = []
    for key, val in a_dictionary.items():
        if val == value:
            key_list.append(key)
    for i in range(len(key_list)):
        del a_dictionary[key_list[i]]
    return a_dictionary
