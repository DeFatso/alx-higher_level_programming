#!/usr/bin/python3
"""
reads a text file
"""


def read_file(filename=""):
    """ raeds file """
    with open(filename) as file:
        for line in file:
            print(line, end='')
