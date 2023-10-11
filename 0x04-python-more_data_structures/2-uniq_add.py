#!/usr/bin/python3
from functools import reduce


def uniq_add(my_list=[]):
    result = reduce(
            lambda distinct, current: distinct + [
                current] if current not in distinct else distinct, my_list, [])
    return sum(result)
