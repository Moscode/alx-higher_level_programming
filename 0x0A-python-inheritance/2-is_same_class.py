#!/usr/bin/python3
"""
Method to determine if it's an instance
"""


def is_same_class(obj, a_class):
    """
        Args:
            obj (object): to test
            a_class (class): to compare to
        Returns (Boolean): True or False
    """
    if type(obj) == a_class:
        return True
    return False
