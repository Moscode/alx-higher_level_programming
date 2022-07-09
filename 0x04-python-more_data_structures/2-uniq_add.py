#!/usr/bin/python3
"""
Function to addd unique element together
"""


def uniq_add(my_list=[]):
    """Add only unique value
        Args:
            my_list (list): list to check
        Returns total (int): total sum of unique to value
    """
    seen_before = []
    total = 0
    for i in range(len(my_list)):
        if my_list[i] in seen_before:
            continue
        else:
            total += my_list[i]
            seen_before.append(my_list[i])
    return total
