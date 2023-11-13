import unittest
import io
from models.square import Square

class TestSquare(unittest.TestCase):
    def test_attributes(self):
        s = Square(5, 2, 3, 1)

        self.assertEqual(s.id, 1)
        self.assertEqual(s.size, 5)
        self.assertEqual(s.x, 2)
        self.assertEqual(s.y, 3)

    def test_area(self):
        s = Square(7, 4, 2)
        self.assertEqual(s.area(), 49)

    def test_display(self):
        s = Square(3, 1, 2)
        expected_output = "###\n ###\n ###"
        
        with unittest.mock.patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            s.display()
            self.assertEqual(mock_stdout.getvalue().strip(), expected_output)

    def test_str(self):
        s = Square(4, 1, 2, 8)
        self.assertEqual(str(s), "[Square] (8) 1/2 - 4")

    def test_update(self):
        s = Square(5, 2, 3, 1)
        s.update(7, 8, 4, 2)

        self.assertEqual(s.id, 7)
        self.assertEqual(s.size, 8)
        self.assertEqual(s.x, 2)
        self.assertEqual(s.y, 3)

    def test_update_kwargs(self):
        s = Square(5, 2, 3, 1)
        s.update(size=8, x=4, y=2)

        self.assertEqual(s.size, 8)
        self.assertEqual(s.x, 4)
        self.assertEqual(s.y, 2)

    def test_to_dictionary(self):
        s = Square(5, 2, 3, 1)
        expected_dict = {'id': 1, 'size': 5, 'x': 2, 'y': 3}
        self.assertEqual(s.to_dictionary(), expected_dict)

if __name__ == '__main__':
    unittest.main()
