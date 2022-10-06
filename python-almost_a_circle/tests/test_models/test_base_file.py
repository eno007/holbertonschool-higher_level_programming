#!/usr/bin/python3
"""Unittest for Base class"""

import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """Tests for Base class"""
    def test_base(self):
        b = Base()
        self.assertEqual(b.id, 1)

if __name__ == '__main__':
    unittest.main()
