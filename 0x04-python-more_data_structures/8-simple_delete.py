#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    for k, v in a_dictionary.items():
        if key == k:
            del a_dictionary[k]
            return a_dictionary
    return a_dictionary
