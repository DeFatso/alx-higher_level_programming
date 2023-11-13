# tests/test_base.py
import unittest
from models.base import Base

class TestBase(unittest.TestCase):

    def test_default_id(self):
        b1 = Base()
        self.assertEqual(b1.id, 1)

    def test_incremented_id(self):
        b1 = Base()
        b2 = Base()
        self.assertEqual(b2.id, b1.id + 1)

    def test_custom_id(self):
        b1 = Base(10)
        self.assertEqual(b1.id, 10)

    def test_mixed_ids(self):
        b1 = Base()
        b2 = Base(5)
        b3 = Base()
        expected_id = b2.id
        self.assertEqual(b3.id, expected_id)

if __name__ == '__main__':
    unittest.main()
