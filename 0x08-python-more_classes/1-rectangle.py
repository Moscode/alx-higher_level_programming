#!/usr/bin/python3
"""
Rectangle is modelling of the math geometry shapee rectangle
"""


class Rectangle:
    """Rectangle Class"""
    def __init__(self, width=0, height=0):
        """Initialize instance attributes once called
            Args:
                width (int, >= 0): set width size
                height (int, >= 0): set height size
        """
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        self.__width = width
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height

    @property
    def width(self):
        """Getter for width private instance attribute
            Returns (int, >= 0): width value
        """
        return self.__width

    @width.setter
    def width(self, width):
        """ Setter for width private instance attribute
            Args:
                width (int, >= 0): set the value of width
        """
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        self.__width = width

    @property
    def height(self):
        """Getter for height private instance attribute
            Returns (int, >= 0): height value
        """
        return self.__height

    @height.setter
    def height(self, height):
        """Setter for height private instance attribute
            Args:
                height (int, >= 0): set the value of height
        """
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height
