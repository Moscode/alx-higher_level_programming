#!/usr/bin/python3
"""
Appending to a file
"""


def append_write(filename="", text=""):
    """Function to append to file
        Args:
            filename (file): file to append to
            text (string): content to append
        Return (int): number of characters append
    """
    with open(filename, "a", encoding="UTF8") as f:
        append_file = f.write(text)
        return append_file
