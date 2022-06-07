#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    first = len(tuple_a)
    second = len(tuple_b)
    if(first >= 1):
        a = tuple_a[0]
    else:
        a = 0
    if(second >= 1):
        b = tuple_b[0]
    else:
        b = 0
    if(first >= 2):
        c = tuple_a[1]
    else:
        c = 0
    if(second >= 2):
        d = tuple_b[1]
    else:
        d = 0
    new_tuple = (a + b, c + d)
    return new_tuple
