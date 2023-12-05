#!/usr/bin/python3
"""Contains the append after function. """


def append_after(filename="", search_string="", new_string=""):
    """Inserts a line of text to a file,
    after each line containing a specific string.
    """
    with open(filename, "r", encoding="utf-8") as myFile, \
         open("tmp.txt", "w", encoding="utf-8") as tmpFile:
        for line in myFile:
            tmpFile.write(line)
            if search_string in line:
                tmpFile.write(new_string)

    with open(filename, "w", encoding="utf-8") as myFile, \
         open("tmp.txt", "r", encoding="utf-8") as tmpFile:
        for line in tmpFile:
            myFile.write(line)
