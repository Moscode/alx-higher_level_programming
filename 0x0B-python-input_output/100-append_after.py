#!/usr/bin/python3
"""

"""


def append_after(filename="", search_string="", new_string=""):
    """

    """
    text = ""
    with open(filename, "r", encoding="UTF8") as f:
        for line in f:
            text += line
            if search_string in line:
                text += new_string
    with open(filename, "w", encoding="UTF8") as f:
        f.write(text)
