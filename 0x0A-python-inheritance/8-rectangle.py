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
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

"""
class Rectangle that inherited from BaseGeometry
"""

class Rectangle(BaseGeometry):
    """
    Rectangle subclass to BaseGeometry
    """

    def __init__(self, width, height):
        """Assign width and height as private attribute

            Args:
                width (int): width of Rectangle
                height (int): height of Rectangle
        """
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height
