#!/usr/bin/python3
def safe_print_integer(value):
    try:
        i = 0
        add = i + value
        print("{:d}".format(value))
    except Exception:
        return False
    else:
        return True
