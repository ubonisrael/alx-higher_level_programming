#!/usr/bin/python3
""" COntains the read_file function. """


def read_file(filename=""):
    """ Reads a file and prints it to stdout. """
    with open(filename, "r", encoding="utf-8") as myFile:
        print(myFile.read(), end="")
