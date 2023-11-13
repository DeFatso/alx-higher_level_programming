#!/usr/bin/python3

import unittest
import sys
import io
from models.square import Square

class TestSquare(unittest.TestCase):
    def test_constructor_with_id(self):
        square = Square(5, id=1)
        self.assertEqual(square.id, 1)
        self.assertEqual(square.size, 5)
        self.assertEqual(square.x, 0)
        self.assertEqual(square.y, 0)

    def test_constructor_without_id(self):
        square = Square(3)
        self.assertIsNotNone(square.id)
        self.assertEqual(square.size, 3)
        self.assertEqual(square.x, 0)
        self.assertEqual(square.y, 0)

    def test_size_setter(self):
        square = Square(4)
        square.size = 7
        self.assertEqual(square.size, 7)

    def test_x_and_y_setter(self):
        square = Square(2)
        square.x = 3
        square.y = 4
        self.assertEqual(square.x, 3)
        self.assertEqual(square.y, 4)

    def test_area(self):
        square = Square(5)
        self.assertEqual(square.area(), 25)

    def test_display(self):
        square = Square(3)
        expected_output = "###\n###\n###\n"
        with io.StringIO() as mock_stdout:
            sys.stdout = mock_stdout
            square.display()
            sys.stdout = sys.__stdout__
            self.assertEqual(mock_stdout.getvalue(), expected_output)

    def test_str_representation(self):
        square = Square(4, id=2, x=1, y=3)
        expected_str = "[Square] (2) 1/3 - 4"
        self.assertEqual(str(square), expected_str)

    def test_to_dictionary(self):
        square = Square(3, id=5, x=2, y=1)
        expected_dict = {'id': 5, 'size': 3, 'x': 2, 'y': 1}
        self.assertEqual(square.to_dictionary(), expected_dict)

    def test_update(self):
        square = Square(2)
        square.update(1, 4, 5, 2)
        self.assertEqual(square.id, 1)
        self.assertEqual(square.size, 4)

    def test_update_kwargs(self):
        square = Square(2)
        square.update(size=5, id=3, x=1, y=2)
        self.assertEqual(square.id, 3)
        self.assertEqual(square.size, 5)
        self.assertEqual(square.x, 1)
        self.assertEqual(square.y, 2)

if __name__ == "__main__":
    unittest.main()
