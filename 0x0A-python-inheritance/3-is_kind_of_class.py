#!/usr/bin/python3

"""
Function to check if obj is an instance of, or instance of a class inherited
"""


def is_kind_of_class(obj, a_class):
    """ Returns True if obj is from a_cilass or is inheritance class
        Args:
            obj: value to validate
            a_class: value to compare with
    """
    if isinstance(obj, a_class):
        return True
    return False
