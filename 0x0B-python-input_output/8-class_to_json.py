#!/usr/bin/python3
"""
Function that takes an instance instance of a class and
return string form of all attributes
"""


def class_to_json(obj):
    """ Functon for Json serialization
    Args:
        obj (object): instance of a classs
    Returns (string): json serialization of an object
    """
    return obj.__dict__
