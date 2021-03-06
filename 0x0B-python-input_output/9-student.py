#!/usr/bin/python3
"""
No imported module
"""


class Student:
    """ Class Student"""

    def __init__(self, first_name, last_name, age):
        """
            Initialize object with attributes
            Args:
                first_name (string): first name of object
                last_name (string): second name of object
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        return self.__dict__
