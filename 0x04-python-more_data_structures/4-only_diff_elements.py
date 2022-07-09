#!/usr/bin/python3
"""
Function to get elements in set_1 or set_2 but not both
"""


def only_diff_elements(set_1, set_2):
    """ Element in set_1 or set_2 but not both
        Args:
            set_1 (set): first set
            set_2 (set): second set
        Returns (set): element first set or second set but not both
    """
    return set_1 ^ set_2
