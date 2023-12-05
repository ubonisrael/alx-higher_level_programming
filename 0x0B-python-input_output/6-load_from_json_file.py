#!/usr/bin/python3
"""contains the load from json function. """


def load_from_json_file(filename):
    """creates an object from a json file"""
    import json

    with open(filename, "r", encoding="utf-8") as myFile:
        my_obj = json.loads(myFile.read())
    return my_obj
