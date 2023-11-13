#!/usr/bin/python3
import io
from unittest.mock import patch
import unittest
from models.rectangle import Rectangle

class TestRectangle(unittest.TestCase):

    def test_constructor_with_id(self):
        # Test if the id is assigned correctly when provided
        rectangle = Rectangle(10, 20, 5, 7, id=1)
        self.assertEqual(rectangle.id, 1)

    def test_constructor_without_id(self):
        # Test if the id is incremented correctly when not provided
        rectangle1 = Rectangle(10, 20, 5, 7)
        rectangle2 = Rectangle(15, 25, 3, 8)
        self.assertEqual(rectangle1.id, rectangle2.id - 1)

    def test_width_height_x_y_properties(self):
        # Test if width, height, x, and y are set correctly
        rectangle = Rectangle(10, 20, 5, 7)
        self.assertEqual(rectangle.width, 10)
        self.assertEqual(rectangle.height, 20)
        self.assertEqual(rectangle.x, 5)
        self.assertEqual(rectangle.y, 7)

    def test_width_height_x_y_setters(self):
        # Test if width, height, x, and y setters work correctly
        rectangle = Rectangle(10, 20, 5, 7)

        rectangle.width = 15
        rectangle.height = 25
        rectangle.x = 3
        rectangle.y = 8

        self.assertEqual(rectangle.width, 15)
        self.assertEqual(rectangle.height, 25)
        self.assertEqual(rectangle.x, 3)
        self.assertEqual(rectangle.y, 8)

    def test_display(self):
        # Test if the display method prints the rectangle correctly
        rectangle = Rectangle(3, 2)
        expected_output = "###\n###\n"
        with patch("sys.stdout", new_callable=io.StringIO) as mock_stdout:
            rectangle.display()
            self.assertEqual(mock_stdout.getvalue(), expected_output)


    def test_area_default_values(self):
        # Test if area method calculates the area with default values correctly
        rectangle = Rectangle(3, 2)
        self.assertEqual(rectangle.area(), 6)


    def test_area_large_dimensions(self):
        # Test if area method calculates the area with large dimensions correctly
        rectangle = Rectangle(1000, 500)
        self.assertEqual(rectangle.area(), 500000)


if __name__ == '__main__':
    unittest.main()
