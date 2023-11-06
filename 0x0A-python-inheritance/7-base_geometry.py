#!/usr/bin/python3

"""
module that has class BaseGeometry
"""


class BaseGeometry:
    """ base class """

    def area(self):
        """ raises exeption """

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """that validates value"""

        if not isinstance(value, int):
            raise TypeError(name + " must be an integer")
        if value <= 0:
            raise ValueError(name + " must be greater than 0")
