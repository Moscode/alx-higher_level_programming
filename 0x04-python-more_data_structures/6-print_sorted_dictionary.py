#!/usr/bin/python3
"""

"""


def print_sorted_dictionary(a_dictionary):
    """

    """
    key_list = list(a_dictionary)
    value_list = []
    sorted_key = sorted(key_list)
    for key in sorted_key:
        value_list.append(a_dictionary[key])
    new_dict = {}
    for i in range(len(sorted_key)):
        new_dict[sorted_key[i]] = value_list[i]
    print(new_dict)
