#!/usr/bin/python3
""" returns peak number from a list """


def find_peak(list_of_integers):
    """ check if list is not empty"""
    if not list_of_integers:
        return None

    peak = list_of_integers[0]

    for i in list_of_integers:
        if i > peak:
            peak = i
    return peak
