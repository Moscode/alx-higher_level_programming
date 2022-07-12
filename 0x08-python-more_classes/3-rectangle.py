#!/usr/bin/python3
"""
Rectangle is modelling of the math geometry shapee rectangle
"""


class Rectangle:
    """Rectangle class"""
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

    def area(self):
        """Calculate area of a rectangle
            Returns (int): area value
        """
        return self.__height * self.__width

    def perimeter(self):
        """Calculate perimeter of a rectangle
            Returns (int): perimeter value
        """
        if (self.__height == 0 or self.__width == 0):
            return 0
        perimeter = 2 * (self.__height + self.__width)
        return perimeter

    def __str__(self):
        if (self.__height == 0 or self.__width == 0):
            return ""
        rect = []
        for h in range(self.__height):
            for w in range(self.__width):
                rect.append("#")
            if h < self.__height - 1:
                rect.append("\n")
        return "".join(rect)
