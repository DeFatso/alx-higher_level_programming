import io
import unittest
from unittest.mock import patch
from models.rectangle import Rectangle

class TestRectangle(unittest.TestCase):
    def test_attributes(self):
        r = Rectangle(10, 20, 2, 3, 1)

        self.assertEqual(r.id, 1)
        self.assertEqual(r.width, 10)
        self.assertEqual(r.height, 20)
        self.assertEqual(r.x, 2)
        self.assertEqual(r.y, 3)

    def test_area(self):
        r = Rectangle(5, 10)
        self.assertEqual(r.area(), 50)

    def test_display(self):
        r = Rectangle(3, 2)
        expected_output = "###\n###"
        
        with unittest.mock.patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            r.display()
            self.assertEqual(mock_stdout.getvalue().strip(), expected_output)

    def test_str(self):
        r = Rectangle(4, 5, 1, 2, 8)
        self.assertEqual(str(r), "[Rectangle] (8) 1/2 - 4/5")

    def test_update(self):
        r = Rectangle(10, 20, 2, 3, 1)
        r.update(7, 15, 25, 4, 5)

        self.assertEqual(r.id, 7)
        self.assertEqual(r.width, 15)
        self.assertEqual(r.height, 25)
        self.assertEqual(r.x, 4)
        self.assertEqual(r.y, 5)

    def test_update_kwargs(self):
        r = Rectangle(10, 20, 2, 3, 1)
        r.update(width=15, height=25, x=4, y=5)

        self.assertEqual(r.width, 15)
        self.assertEqual(r.height, 25)
        self.assertEqual(r.x, 4)
        self.assertEqual(r.y, 5)

if __name__ == '__main__':
    unittest.main()
