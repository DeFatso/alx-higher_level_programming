#!/usr/bin/python3
def raise_exception():
    raise TypeError("This is a custom TypeError")

    try:
        raise_exception()
    except TypeError as te:
        print("Exception raised")
