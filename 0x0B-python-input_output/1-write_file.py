#!/usr/bin/python3
"""Contains the write_file function. """


def write_file(filename="", text=""):
    """ Writes a string to a text file and returns the number of
    chars written.
    """
    with open(filename, "w", encoding="utf-8") as myFile:
        wr = myFile.write(text)

    return wr
