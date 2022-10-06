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
    def setUpClass(cls):
        """sets up class"""
        Base._Base__nb_objects = 0
        cls.b1 = Base()
        self.assertEqual(b1.id)
        cls.b2 = Base()
        self.assertEqual(b2.id, 1)
        cls.b3 = Base(89)
        self.assertEqual(b3.id, 89)


if __name__ == '__main__':
    unittest.main()
