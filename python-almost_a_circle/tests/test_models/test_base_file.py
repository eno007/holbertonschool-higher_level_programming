import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """Tests for Base class"""
    def test_base(self):
        b = Base()
        self.assertEqual(b.id, 1)
        b = Base()
        self.assertEqual(b.id, 2)
        b = Base(89)
        self.assertEqual(b.id, 89)

if __name__ == '__main__':
    unittest.main()
