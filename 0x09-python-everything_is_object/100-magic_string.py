#!/usr/bin/python3
def magic_string():
    magic_number = getattr(magic_string, "n", 0) + 1
    return ("BestSchool, " * (magic_number - 1) + "BestSchool")
