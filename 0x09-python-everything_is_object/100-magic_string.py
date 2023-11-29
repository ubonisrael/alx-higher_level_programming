#!/usr/bin/python3
def magic_string():
    magic_string.a = getattr(magic_string, 'a', 0) + 1
    return ("BestSchool" + ((magic_string.a - 1) * ", BestSchool"))
