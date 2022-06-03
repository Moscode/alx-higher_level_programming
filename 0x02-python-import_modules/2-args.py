#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    size = len(argv)
    print("{:d} {:s}{:s}".format(size - 1,
          "argument" if size == 2 else "arguments",
                                 "." if size == 1 else ":"))
    for i, s in enumerate(argv):
        if i > 0:
            print("{:d}: {:s}".format(i, s))
