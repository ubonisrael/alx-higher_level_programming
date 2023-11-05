#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if not my_list:
        pass
    else:
        length = len(my_list) - 1
        if length >= 0:
            while length >= 0:
                print("{:d}".format(my_list[length]))
                length -= 1
