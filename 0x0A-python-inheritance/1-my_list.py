#!/usr/bin/python3
"""
Class for a list of numbers, sorting it in ascending order
"""


class MyList(list):
    """
    class derived from list class
    """
    def print_sorted(self):
        """Print the sorted version for numbers
        """
        self.sort()
        print(self)
