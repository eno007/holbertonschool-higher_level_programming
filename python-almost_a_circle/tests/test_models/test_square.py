#!/usr/bin/python3
import unittest
from models.square import Square


class TestSquare(unittest.TestCase):
    """Test class for square class"""
    def test_square_one(self):
        """test 1 arg"""
        sq1 = Square(1)
        sq2 = Square(2)
        self.assertEqual(sq1.id, sq2.id - 1)

    def test_square_two(self):
        """test 2 args"""
        sq1 = Square(1, 2)
        sq2 = Square(2, 3)
        self.assertEqual(sq1.id, sq2.id - 1)

    def test_square_three(self):
        """test 3 args"""
        sq1 = Square(1, 2, 3)
        sq2 = Square(1, 3, 4)
        self.assertEqual(sq1.id, sq2.id - 1)

    def test_square_four(self):
        """test 4 args"""
        sq1 = Square(1, 2, 3, 10)
        sq2 = Square(3, 4, 5, 11)
        self.assertEqual(sq1.id, sq2.id - 1)

    def test_square_str_size(self):
        with self.assertRaises(TypeError):
            sq1 = Square("one")

    def test_square_str_arg(self):
        with self.assertRaises(TypeError):
            sq1 = Square(1, "two")

    def test_square_str_x(self):
        with self.assertRaises(TypeError):
            sq1 = Square(1, 2, "three")

    def test_negative_size(self):
        with self.assertRaises(ValueError):
            sq1 = Square(-1)

    def test_negative_arg(self):
        with self.assertRaises(ValueError):
            sq1 = Square(1, -2)

    def test_negative_x(self):
        with self.assertRaises(ValueError):
            sq1 = Square(1, 2, -3)

    def test_zero_size(self):
        with self.assertRaises(ValueError):
            sq1 = Square(0)

    def test_str_method(self):
        sq1 = Square(3, 1, 2, 10)
        self.assertEqual("[Square] (10) 1/2 - 3", sq1.__str__())

    def test_update_method1(self):
        sq1 = Square(3, 1, 2, 10)
        sq1.update(89)
        self.assertEqual(89, sq1.id)

    def test_update_method2(self):
        sq1 = Square(3, 1, 2, 10)
        sq1.update(89, 1)
        self.assertEqual(89, sq1.id)
        self.assertEqual(1, sq1.size)

    def test_update_method2(self):
        sq1 = Square(3, 1, 2, 10)
        sq1.update(89, 1, 2)
        self.assertEqual(89, sq1.id)
        self.assertEqual(1, sq1.size)
        self.assertEqual(2, sq1.x)

    def test_update_method2(self):
        sq1 = Square(3, 1, 2, 10)
        sq1.update(89, 1, 2, 3)
        self.assertEqual(89, sq1.id)
        self.assertEqual(1, sq1.size)
        self.assertEqual(2, sq1.x)
        self.assertEqual(3, sq1.y)

    def test_to_dect(self):
        sq1 = Square(3, 1, 2, 10)
        dict1 = {'size': 3, 'x': 1, 'y': 2, 'id': 10}
        self.assertEqual(dict1, sq1.to_dictionary())

    def test_create(self):
        dict1 = {'size': 3, 'x': 1, 'y': 2, 'id': 10}
        sq1 = Square.create(**dict1)

    def test_save_to_file(self):
        Square.save_to_file([Square(1)])
        with open("Square.json", "r") as my_file:
            string = my_file.read()
            self.assertEqual(str, type(string))

    def test_save_to_file_None(self):
        Square.save_to_file(None)
        with open("Square.json", "r") as my_file:
            self.assertEqual("[]", my_file.read())

    def test_save_to_file_empty(self):
        Square.save_to_file([])
        with open("Square.json", "r") as my_file:
            self.assertEqual("[]", my_file.read())

    def test_load_from_file(self):
        sq1 = Square(3, 1, 2, 10)
        Square.save_to_file([sq1])
        sqList = Square.load_from_file()
        self.assertEqual(str(sq1), str(sqList[0]))
