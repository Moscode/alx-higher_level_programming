#!/usr/bin/python3

"""
class with public instance method
"""


class BaseGeometry:
    """
    BaseGeometry with a method
    """
    def area(self):
        """
        Area method doing nothing yet
        """
        raise Exception("area() is not implemented")
    def integer_validator(self, name, value):
        if not isinstance(value, int):
            raise TypeError("<name> must be an integer")
        if value <= 0:
            raise ValueError(name + " must be greater than 0")
