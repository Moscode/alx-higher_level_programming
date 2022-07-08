#!/usr/bin/python3

"""Import sys"""
import sys

"""Import save_to_json_file"""
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file

"""Import load_from_json_file"""
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

"""
Saving command line argument into a json file without the element at index 0
"""


try:
    contents = load_from_json_file("add_item.json")
except FileNotFoundError:
    contents = []
contents.extend(sys.argv[1:])
save_to_json_file(contents, "add_item.json")
