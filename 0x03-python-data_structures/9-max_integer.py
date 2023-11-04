#!/usr/bin/python3
def max_integer(my_list=[]):
    max_val = 0
    length = len(my_list)
    if length == 0:
        return None
    for val in my_list:
        if val > max_val:
            max_val = val
    return max_val
