class LockedClass():
    def __init__(self):
        first_name = "Moses"

    def __setattr__(self, first_name, value):
        if not first_name in self.__dict__:
            return
