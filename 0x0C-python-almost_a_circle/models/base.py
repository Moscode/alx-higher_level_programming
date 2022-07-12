#!/usr/bin/python3
"""Base class"""


class Base:
    """ Module of a base"""
    __nb_objects = 0

    def __init__(self, id=None):
        """ For initiaizing id
            
            Args:
                id (int): identification number for each instance

            Returns: None
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
