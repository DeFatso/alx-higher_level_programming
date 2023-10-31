#!/usr/bin/python3
def add_integer(a, b=98):
    """adds integers"""
    if not (isinstance(a, int) or isinstance(a, float)):
        raise TypeError("a must be an integer")
    if not (isinstance(b, int) or isinstance(b, float)):
        raise TypeError("b must be an integer")

    result = a + b
    return int(result)


if __name__ == "__main__":
    import doctest
    doctest.testfile("0-add_integer.py")
