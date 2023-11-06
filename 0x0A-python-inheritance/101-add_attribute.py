#!/usr/bin/python3

def add_attribute(obj, attr_name, attr_value):
    """ adds attribute if possible"""

    if not hasattr(obj, '__dict__') and not hasattr(obj, '__slots__'):
        raise TypeError("can't add new attribute")

    setattr(obj, attr_name, attr_value)
