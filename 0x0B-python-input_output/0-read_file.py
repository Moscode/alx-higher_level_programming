#!/usr/bin/python3
"""
Function that read a file
"""


def read_file(filename=""):
    """Print content of file out on stdout
        Args:
            filename (file): encoding using UTF8
    """

    with open(filename, "r", encoding="UTF8") as f:
        read_file = f.read()
    print(read_file, end="")
