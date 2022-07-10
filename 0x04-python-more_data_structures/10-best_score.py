#!/usr/bin/python3
"""
Find max score using dictionary
"""


def best_score(a_dictionary):
    """ Find max score using values in dictionary
        Args:
            a_dictionary (dict): dictionary to check through
        Returns (int): max score
    """
    if not isinstance(a_dictionary, dict) or len(a_dictionary) == 0:
        return None
    max_score = 0
    max_key = ""
    for key, value in a_dictionary.items():
        if value > max_score:
            max_score = value
            max_key = key
    return max_key
