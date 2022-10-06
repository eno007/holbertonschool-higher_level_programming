#!/usr/bin/python3
"""Unittest for Base class"""

import json
import os
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    """Tests for Base class"""
    @classmethod
    def test_constantId(self):
        """Test of Base for correctly initializing an id"""
        b = Base(9)
        self.assertEqual(b.id, 9)

    def test_autoId(self):
        """Test of Base for automatically assigning and incrementing an id"""
        b = Base()
        self.assertEqual(b.id, 1)

    def test_string(self):
        """Test of Base for case input is string"""
        b = Base("string")
        self.assertEqual(b.id, "string")

if __name__ == '__main__':
    unittest.main()
