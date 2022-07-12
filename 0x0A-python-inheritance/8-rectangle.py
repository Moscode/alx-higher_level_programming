#!/usr/bin/python3
"""Import class from another class"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


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
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
