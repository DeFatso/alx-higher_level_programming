#!/usr/bin/python3
"""
writes text file
"""


def write_file(filename="", text=""):
    """ writes a string to a text file """

    with open(filename, "w") as file:
        length = file.write(text)

        return length
