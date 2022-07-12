#!/usr/bin/python3
for i in range(100):
    if i < 10:
        i = "0{}".format(i)
        print("{}".format(i), end=", ")
    else:
        print("{}".format(i), end=", " if i < 99 else None)
