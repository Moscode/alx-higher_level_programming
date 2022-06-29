class LockedClass():
    """Class and instances cannot dynamically create attribute
        except first_name
    """
    def __init__(self):
        first_name = "Moses"

    def __setattr__(self, first_name, value):
        if not first_name in self.__dict__:
            return
