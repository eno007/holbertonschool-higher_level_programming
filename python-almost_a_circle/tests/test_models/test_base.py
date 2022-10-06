import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """Tests for Base class"""
    def test_base(self):
        b0 = Base()
        self.assertEqual(b0.id, 1)
        b1 = Base()
        self.assertEqual(b1.id, 2)
        b2 = Base(89)
        self.assertEqual(b2.id, 89)
