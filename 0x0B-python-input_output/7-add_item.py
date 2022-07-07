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


save_to_json_file(sys.argv, "add_item.json")
oriList = load_from_json_file("add_item.json")
del oriList[0]
save_to_json_file(oriList, "add_item.json")
