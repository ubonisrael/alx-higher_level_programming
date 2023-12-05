#!/usr/bin/python3
"""Contains the append_write function. """


def append_write(filename="", text=""):
    """appends a string at the end of a text file. """
    with open(filename, "a", encoding="utf-8") as myFile:
        wr = myFile.write(text)
    return wr
