#!/usr/bin/python3
"""
Write to a file
"""


def write_file(filename="", text=""):
    """ Function to write to filename
        Args:
            filename (file): holding file address
            text (string): holding the string to store
        Returns (int): number of count in filename
    """
    with open(filename, "w", encoding="UTF8") as f:
        return f.write(text)
