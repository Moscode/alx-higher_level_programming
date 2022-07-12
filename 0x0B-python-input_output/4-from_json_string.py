#!/usr/bin/python3

"""Import Json module"""
import json
"""
Function to convert json to object (python data structure) and return it
"""


def from_json_string(my_str):
    """ Take json convert it to object
        Args:
            my_str (json): to be converted to object
        Returns (object): send object
    """
    return json.loads(my_str)
