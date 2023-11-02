#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    length = len(sys.argv)
    count = 0
    x = 1
    print("{} argument{}{}".format(length - 1, 's' if length - 1 != 1 else '',
                                   '.' if length == 1 else ':'))
    if length > 1:
        while x < length:
            print("{}: {}".format(x, sys.argv[x]))
            x += 1
