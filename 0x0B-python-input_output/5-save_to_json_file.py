#!/usr/bin/python3
"""import json"""
import json

"""
Function to change from object to json
"""


def save_to_json_file(my_obj, filename):
    """ Write string as json representation in file with json extension
        Args:
            my_obj (string): string to store as Json representation
            filename (json): file with json extension
    """
    with open(filename, "w") as f:
        json.dump(my_obj, f)
