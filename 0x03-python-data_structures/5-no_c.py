#!/usr/bin/python3
def no_c(my_string):
    str_len = len(my_string)
    if str_len == 0:
        return
    new_str = ''
    for ch in my_string:
        if ch != 'c' and ch != 'C':
            new_str += ch
    return new_str
