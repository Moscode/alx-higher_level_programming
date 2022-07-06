#!/usr/bin/python3

"""Import json module"""
import json
"""
Function to covert string to json and return the json representation
"""


def to_json_string(my_obj):
    """Function to convert string to json format
        Args:
            my_obj (string): string to print out json representation
        Returns (json): json representation
    """
    return json.dumps(my_obj)
