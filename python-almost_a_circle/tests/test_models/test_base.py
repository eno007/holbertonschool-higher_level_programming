#!/usr/bin/python3
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

    def test_id_negative(self):
        """test if id is negative"""
        base1 = Base(-89)
        self.assertEqual(-89, base1.id)

    def test_id_string(self):
        """test if id is string"""
        base1 = Base("id")
        self.assertEqual("id", base1.id)

    def test_id_zero(self):
        """test if id is 0"""
        base1 = Base(0)
        self.assertEqual(0, base1.id)

    def test_to_json_none(self):
        """test method to json none"""
        json_str = Base.to_json_string(None)
        self.assertEqual(json_str, "[]")

    def test_from_json(self):
        """test method from json none"""
        json_list = Base.from_json_string(None)
        self.assertEqual(json_list, [])
