#!/usr/bin/python3
"""
No imported module
"""


class Student:
    """ Class Student"""

    def __init__(self, first_name, last_name, age):
        """
            Initialize object with attributes
            Args:
                first_name (string): first name of object
                last_name (string): second name of object
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ Filter dict using list
            Args:
                attrs (list): each props there should be used as a filter
            Returns (dict): return the filter attributes based on args
        """
        if attrs is not None:
            newDict = {}
            listForName = list(self.__dict__)
            for i in range(len(attrs)):
                for j in range(len(listForName)):
                    if attrs[i] == listForName[j]:
                        newDict[listForName[j]] = self.__dict__[listForName[j]]
            return newDict
        return self.__dict__

    def reload_from_json(self, json):
        """Reset attributes for the object
            Arg (dict): props and values
        """
        for key, value in json.items():
            setattr(self, key, value)
