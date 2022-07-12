#!/usr/bin/python3
"""
Returns all attributes and methods of the object
"""


def lookup(obj):
    """ Returns all attributes and methods of an object
        Args:
            obj (object): to check the attr and methods
    """
    return dir(obj)
