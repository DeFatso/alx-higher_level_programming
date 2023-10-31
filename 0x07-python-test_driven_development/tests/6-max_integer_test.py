#!/usr/bin/python3

import unittest


def max_integer(list=[]):
    """ return max in a list"""

    return max(list)


class Test_max(unittest.TestCase):
    """class test case"""

    def test_positive(self):
        """ tests with positive numbers"""
        self.assertEqual(max_integer([1, 2, 3, 4, 5]), 5)

    def test_negative(self):
        """ with negative numbers"""
        self.assertEqual(max_integer([-1, -2, -3, -4, -5]), -1)

    def test_mixed(self):
        """ with mixed"""
        self.assertEqual(max_integer([-1, 2, -3, 4, -5]), 4)

    def test_single(self):
        """ with one number"""
        self.assertEqual(max_integer([17]), 17)


if __name__ == '__main__':
    unittest.main()
