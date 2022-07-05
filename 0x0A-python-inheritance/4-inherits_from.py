#!/usr/bin/python3

"""
Function that returns True if obj is an instance else return False
"""


def inherits_from(obj, a_class):
    """Check if obj is inherited from a_class directly or indirectly
        Args:
            obj: object to check
            a_class: class to compare to
        Returns: True if same other False
    """
    if type(obj) == a_class:
        return True
    return False
