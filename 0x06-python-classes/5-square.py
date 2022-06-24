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
    public instance method for area
    """
    def area(self):
        return self.__size ** 2
    """
    public instance method for print a square
    """
    def my_print(self):
        if (self.__size == 0):
            print(" ")
        for i in range(self.__size):
            print("#" * self.__size)
