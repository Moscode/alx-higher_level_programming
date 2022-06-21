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
    new feature: public instance method
    """
    def area(self):
        return self.__size ** 2
