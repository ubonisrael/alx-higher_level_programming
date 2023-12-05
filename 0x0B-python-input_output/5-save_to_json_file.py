#!/usr/bin/python3
"""Contains the save_to_json_file. """


def save_to_json_file(my_obj, filename):
    """writes an object to a text file using a json string. """
    import json

    with open(filename, "w", encoding="utf-8") as myFile:
        myFile.write(json.dumps(my_obj))
