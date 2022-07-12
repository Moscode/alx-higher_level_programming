#!/usr/bin/python3

""" Import module"""
import json
"""
Create object from a JSON file
"""


def load_from_json_file(filename):
    """
        Args:
            filename (file): json file to read from
    """
    with open(filename) as f:
        return json.load(f)
