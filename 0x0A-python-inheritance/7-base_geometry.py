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
        """
        Validating if the value of pass to value is int and > 0

        Args:
            name (str): name of the parameter to validate
            value (int): parameter to validate
        Raises:
            TypeError: if value is not an integer
            ValueError: if value is <= 0
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
