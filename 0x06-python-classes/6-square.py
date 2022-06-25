#!/usr/bin/python3
"""
This is Square module with new feature
"""


class Square:
    """
    private instance attribute & error handling
    """
    def __init__(self, size=0, position=(0, 0)):
        if (type(size) != int):
            raise TypeError("size must be an integer")
        elif (size < 0):
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
        if (len(position) == 2 and position[0] >= 0 and position[1] >= 0):
            self.__position = position
        else:
            raise TypeError(
                    "position must be a tuple of 2 position integers"
                    )
    """
    getter & setter - size
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
    getter and setter - position
    """
    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if (len(value) == 2 and value[0] > 0 and value[1] > 0):
            self.__value = value
        else:
            raise TypeError(
                    "position must be a tuple of 2 positive integer"
                    )
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
            print("")
        else:
            for i in range(self.__position[1]):
                print("")
            for i in range(self.__size):
                print(" " * self.position[0] + "#" * self.__size)
