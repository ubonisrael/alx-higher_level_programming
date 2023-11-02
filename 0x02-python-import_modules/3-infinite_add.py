#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    length = len(sys.argv)
    x = 1
    total = 0
    if length > 1:
        while x < length:
            total += int(sys.argv[x])
            x += 1
    print("{}".format(total))
