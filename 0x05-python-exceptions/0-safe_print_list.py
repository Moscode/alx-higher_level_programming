#!/usr/bin/python3
class indexLength(Exception):
    def __init__(self, *args, **kwargs):
        Exception.__init__(self, *args, **kwargs)
def safe_print_list(my_list=[], x=0):
    try:
        i = 0
        for value in my_list:
            print("{}".format(value), end='')
            i += 1
        print("")
        if x <= i: 
            return x
        else:
            raise indexLength
    except indexLength:
        return i
