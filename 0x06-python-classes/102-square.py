#!/usr/bin/python3
"""
This is Square module with new feature
"""


class Square:
    """
    private instance attribute & error handling
    """
    def __init__(self, size=0):
        if (type(size) != int):
            raise TypeError("size must be an integer")
        elif (size < 0):
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
    """
    getter & setter
    """
    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if (type(value) != int):
            raise TypeError("size must be an integer")
        elif (value < 0):
            raise ValueError("size must be >= 0")
        else:
            self.__size = value
    """
    public instance method
    """
    def area(self):
        return self.__size ** 2

    def __eq__(self, other):
        """
        == comparison of two squares
        """
        if(isinstance(other, Square)):
            return self.area() == other.area()

    def __ne__(self, other):
        """
        != comparison of two squares
        """
        if(isinstance(other, Square)):
            return self.area() != other.area()

    def __gt__(self, other):
        """
        > comparison of two squares
        """
        if(isinstance(other, Square)):
            return self.area() > other.area()

    def __lt__(self, other):
        """
        < comparison of two squares
        """
        if(isinstance(other, Square)):
            return self.area() < other.area()

    def __ge__(self, other):
        """
        >= comparison of two squares
        """
        if(isinstance(other, Square)):
            return self.area() >= other.area()

    def __le__(self, other):
        """
        <= comparison of two squares
        """
        if(isinstance(other, Square)):
            return self.area() <= other.area()
