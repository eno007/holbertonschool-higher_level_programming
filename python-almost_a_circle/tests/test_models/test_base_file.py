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
        cls.b2 = Base()
        cls.b3 = Base(89)

    def test_id_create_1(self):
        """tests for creation"""
        self.assertTrue(self.b1)

    def test_id_create_2(self):
        """tests for creation"""
        self.assertTrue(self.b3.id, 12)


if __name__ == '__main__':
    unittest.main()
