#!/usr/bin/python3
"""
Search and Update Function
"""


def append_after(filename="", search_string="", new_string=""):
    """open and read file, then open and update
        Args:
            filename (file): file to search and update
            search_string (string): what to check for in file
            new_string (string): what to add to file
    """
    text = ""
    with open(filename, "r", encoding="UTF8") as f:
        for line in f:
            text += line
            if search_string in line:
                text += new_string
    with open(filename, "w", encoding="UTF8") as f:
        f.write(text)
