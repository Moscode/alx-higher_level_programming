#!/usr/bin/python3
class LockedClass():
    """Class and instances cannot dynamically create attribute
        except first_name
    """
    def __init__(self):
        """
        set inial attribute
        """
        first_name = "Moses"
    def __setattr__(self, first_name, value):
        """if attribute is not know don't use it"""

        if not first_name in self.__dict__:
            return
