#!/usr/bin/python3
def max_integer(my_list=[]):
    length = len(my_list)
    if length == 0:
        return None
    max_val = my_list[0]
    for val in my_list:
        if val > max_val:
            max_val = val
    return max_val
