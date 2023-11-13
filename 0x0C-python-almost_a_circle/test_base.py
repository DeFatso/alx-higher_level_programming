# test_base.py

import unittest
from models.base import Base

class TestBase(unittest.TestCase):

    def test_id_assignment(self):
        # Test if the id is assigned correctly when provided
        obj_with_id = Base(5)
        self.assertEqual(obj_with_id.id, 5)

    def test_id_increment(self):
        # Test if the id is incremented correctly when not provided
        obj1 = Base()
        obj2 = Base()
        self.assertEqual(obj1.id, 1)
        self.assertEqual(obj2.id, 2)

    def test_private_attribute(self):
        # Test if the private attribute __nb_objects is not accessible directly
        with self.assertRaises(AttributeError):
            print(Base.__nb_objects)

if __name__ == '__main__':
    unittest.main()
