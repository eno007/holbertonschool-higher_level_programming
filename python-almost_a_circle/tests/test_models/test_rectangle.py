#!/usr/bin/python3
import unittest
from models.rectangle import Rectangle
from io import StringIO
import sys

class TestRectangle(unittest.TestCase):
    """Test class for rectangle class"""
    def test_rectangle_width_height(self):
        """test rectangle with height and height"""
        rect1 = Rectangle(1, 2)
        rect2 = Rectangle(2, 1)
        self.assertEqual(rect1.id, rect2.id - 1)

    def test_rectangle_3_args(self):
        """test rectangle with heigh, weight and x"""
        rect1 = Rectangle(1, 2, 3)
        rect2 = Rectangle(3, 2, 1)
        self.assertEqual(rect1.id, rect2.id - 1)

    def test_rectangle_4_args(self):
        """test rectangle with height, width, x, y"""
        rect1 = Rectangle(1, 2, 3, 4)
        rect2 = Rectangle(2, 3, 4, 5)
        self.assertEqual(rect1.id, rect2.id - 1)

    def test_rectangle_all_args(self):
        """test if rect with all 5 args exists"""
        rect1 = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(5, rect1.id)

    def test_rectangle_width_str(self):
        """test width as str"""
        with self.assertRaises(TypeError):
            rect1 = Rectangle("one", 2)

    def test_rectangle_height_str(self):
        """test height as str"""
        with self.assertRaises(TypeError):
            rect1 = Rectangle(1, "two")

    def test_rect_x_str(self):
        """test rect with x as str"""
        with self.assertRaises(TypeError):
            rect1 = Rectangle(1, 2, "three")

    def test_rect_y_str(self):
        """test rect with y as str"""
        with self.assertRaises(TypeError):
            rect1 = Rectangle(1, 2, 3, "four")

    def test_negative_width(self):
        """test rect with negative width"""
        with self.assertRaises(ValueError):
            rect1 = Rectangle(-1, 2)

    def test_negative_height(self):
        """test rect with negative height"""
        with self.assertRaises(ValueError):
            rect1 = Rectangle(1, -2)

    def test_neg_x(self):
        """test rect with negative x"""
        with self.assertRaises(ValueError):
            rect1 = Rectangle(1, 2, -3)

    def test_neg_y(self):
        """test rect with negative y"""
        with self.assertRaises(ValueError):
            rect1 = Rectangle(1, 2, 3, -4)

    def test_width_zero(self):
        """test rect with width 0"""
        with self.assertRaises(ValueError):
            rect1 = Rectangle(0, 1)

    def test_height_zero(self):
        """test rect with height 0"""
        with self.assertRaises(ValueError):
            rect1 = Rectangle(1, 0)

    def test_area(self):
        """test rect area"""
        rect1 = Rectangle(1, 2)
        self.assertEqual(2, rect1.area())

    def test_str_method(self):
        """test str overload method"""
        rect1 = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual("[Rectangle] (5) 3/4 - 1/2", rect1.__str__())

    def test_display_method(self):
        """test display method"""
        capturedOutput = StringIO()
        sys.stdout = capturedOutput
        rect1 = Rectangle(1, 2)
        rect1.display()
        sys.stdout = sys.__stdout__
        self.assertEqual("#\n#\n", capturedOutput.getvalue())

    def test_display_x_y(self):
        capturedOutput = StringIO()
        sys.stdout = capturedOutput
        rect1 = Rectangle(1, 2, 2, 2)
        rect1.display()
        sys.stdout = sys.__stdout__
        self.assertEqual("\n\n  #\n  #\n", capturedOutput.getvalue())

    def test_update(self):
        """test update method with 1 arg"""
        rect1 = Rectangle(1, 2, 3, 4, 5)
        rect1.update(89)
        self.assertEqual(89, rect1.id)

    def test_update_2(self):
        """test update method with 2 args"""
        rect1 = Rectangle(1, 2, 3, 4, 5)
        rect1.update(89, 1)
        self.assertEqual(89, rect1.id)
        self.assertEqual(1, rect1.width)

    def test_update_3(self):
        """test update with 3 args"""
        rect1 = Rectangle(1, 2, 3, 4, 5)
        rect1.update(89, 1, 2)
        self.assertEqual(89, rect1.id)
        self.assertEqual(1, rect1.width)
        self.assertEqual(2, rect1.height)

    def test_update_4(self):
        """test update with 4 args"""
        rect1 = Rectangle(1, 2, 3, 4, 5)
        rect1.update(89, 1, 2, 3)
        self.assertEqual(89, rect1.id)
        self.assertEqual(1, rect1.width)
        self.assertEqual(2, rect1.height)
        self.assertEqual(3, rect1.x)

    def test_update_5(self):
        """test update with 5 args"""
        rect1 = Rectangle(1, 2, 3, 4, 5)
        rect1.update(89, 1, 2, 3, 4)
        self.assertEqual(89, rect1.id)
        self.assertEqual(1, rect1.width)
        self.assertEqual(2, rect1.height)
        self.assertEqual(3, rect1.x)
        self.assertEqual(4, rect1.y)

    def test_to_dict(self):
        """test to dictionary method"""
        rect1 = Rectangle(1, 2, 0, 0, 0)
        dict1 = {'width': 1, 'height': 2, 'x': 0, 'y': 0, 'id': 0}
        self.assertEqual(dict1, rect1.to_dictionary())

    def test_create(self):
        """test create method"""
        dict1 = {'width': 1, 'height': 2, 'x': 0, 'y': 0, 'id': 10}
        rect1 = Rectangle.create(**dict1)
        self.assertEqual(10, rect1.id)

    def test_save_to_file(self):
        """test save to file method"""
        Rectangle.save_to_file([Rectangle(1, 2)])
        with open("Rectangle.json", "r", encoding="UTF8") as my_file:
            string = my_file.read()
        self.assertEqual(str, type(string))

    def test_save_to_file_None(self):
        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r", encoding="UTF8") as my_file:
            self.assertEqual("[]", my_file.read())

    def test_save_to_empty_file(self):
        Rectangle.save_to_file([])
        with open("Rectangle.json", "r", encoding="UTF8") as my_file:
            self.assertEqual("[]", my_file.read())

    def test_load_from_file(self):
        """test load from file method"""
        rect1 = Rectangle(1, 2, 0, 0, 10)
        Rectangle.save_to_file([rect1])
        rectList = Rectangle.load_from_file()
        self.assertEqual(str(rect1), str(rectList[0]))
