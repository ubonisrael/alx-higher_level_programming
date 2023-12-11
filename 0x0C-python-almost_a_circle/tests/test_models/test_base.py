#!/usr/bin/python3
"""Contains tests for the Base class. """
import unittest
import io
import os
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase_Init(unittest.TestCase):
    """Contains tests for the initialization of the Base class. """

    def test_no_args(self):
        a = Base()
        b = Base()
        self.assertEqual(a.id, b.id - 1)

    def test_three_bases(self):
        a = Base()
        b = Base()
        c = Base()
        self.assertEqual(a.id, c.id - 2)

    def test_unique_id(self):
        a = Base(9)
        self.assertEqual(9, a.id)

    def test_no_args_with_args(self):
        a = Base()
        b = Base(7)
        c = Base(15)
        d = Base()
        self.assertEqual(a.id, d.id - 1)
        self.assertEqual(15, c.id)
        self.assertEqual(7, b.id)

    def test_public_id(self):
        a = Base()
        a.id = 10
        self.assertEqual(a.id, 10)

    def test_private_nb_objects(self):
        with self.assertRaises(AttributeError):
            print(Base().__nb_instances)

    def test_instantation_with_two_args(self):
        with self.assertRaises(TypeError):
            a = Base(2, 2)


class TestBase_To_Json(unittest.TestCase):
    """Contains tests for the to_json_string method of the Base class"""
    def test_type(self):
        r = Rectangle(10, 7, 2, 8, 6)
        self.assertEqual(str, type(Base.to_json_string([r.to_dictionary()])))

    def test_one_dict(self):
        r = Rectangle(10, 7, 2, 8, 6)
        self.assertTrue(len(Base.to_json_string([r.to_dictionary()])) == 53)

    def test_two_dicts(self):
        r1 = Rectangle(2, 3, 5, 19, 2)
        r2 = Rectangle(4, 2, 4, 1, 12)
        list_dicts = [r1.to_dictionary(), r2.to_dictionary()]
        self.assertTrue(len(Base.to_json_string(list_dicts)) == 106)

    def test_square_type(self):
        s = Square(10, 2, 3, 4)
        self.assertEqual(str, type(Base.to_json_string([s.to_dictionary()])))

    def test_square_one_dict(self):
        s = Square(10, 2, 3, 4)
        self.assertTrue(len(Base.to_json_string([s.to_dictionary()])) == 39)

    def test_square_two_dicts(self):
        s1 = Square(10, 2, 3, 4)
        s2 = Square(4, 5, 21, 2)
        list_dicts = [s1.to_dictionary(), s2.to_dictionary()]
        self.assertTrue(len(Base.to_json_string(list_dicts)) == 78)

    def test_empty_list(self):
        self.assertEqual("[]", Base.to_json_string([]))

    def test_string_none(self):
        self.assertEqual("[]", Base.to_json_string(None))

    def test_no_args(self):
        with self.assertRaises(TypeError):
            Base.to_json_string()

    def test_more_than_one_arg(self):
        with self.assertRaises(TypeError):
            Base.to_json_string([], 1)


class TestBase_Save_To_File(unittest.TestCase):
    """Tests for the save_to_file method of the Base class"""
    @classmethod
    def tearDown(self):
        try:
            os.remove("Base.json")
        except IOError:
            pass
        try:
            os.remove("Rectangle.json")
        except IOError:
            pass
        try:
            os.remove("Square.json")
        except IOError:
            pass

    def test_one_rectangle(self):
        a = Rectangle(10, 7, 2, 8)
        Rectangle.save_to_file([a])
        with open("Rectangle.json", "r") as myFile:
            self.assertEqual(len(myFile.read()), 54)

    def test_two_rectangles(self):
        a = Rectangle(10, 7, 2, 8)
        b = Rectangle(2, 4)
        Rectangle.save_to_file([a, b])
        with open("Rectangle.json", "r") as myFile:
            self.assertEqual(len(myFile.read()), 107)

    def test_one_square(self):
        a = Square(10, 2, 8)
        Square.save_to_file([a])
        with open("Square.json", "r") as myFile:
            self.assertEqual(len(myFile.read()), 40)

    def test_two_squares(self):
        a = Square(10, 2, 8)
        b = Square(4)
        Square.save_to_file([a, b])
        with open("Square.json", "r") as myFile:
            self.assertEqual(len(myFile.read()), 79)

    def test_check_filename(self):
        a = Square(10)
        Rectangle.save_to_file([a])
        with open("Rectangle.json", "r") as myFile:
            self.assertEqual(len(myFile.read()), 40)

    def test_file_overwrite(self):
        a = Square(100)
        Square.save_to_file([a])
        b = Square(10)
        Square.save_to_file([b])
        with open("Square.json", "r") as myFile:
            self.assertEqual(len(myFile.read()), 40)

    def test_save_none(self):
        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r") as myFile:
            self.assertEqual(myFile.read(), '[]')

    def test_empty_list(self):
        Rectangle.save_to_file([])
        with open("Rectangle.json", "r") as myFile:
            self.assertEqual(myFile.read(), '[]')

    def test_no_args(self):
        with self.assertRaises(TypeError):
            Base.save_to_file()

    def test_two_args(self):
        with self.assertRaises(TypeError):
            Base.save_to_file([], {1, 2})


class TestBase_From_Json(unittest.TestCase):
    """Runs tests for the from_json_string method of the Base class"""
    def test_type(self):
        list_input = [
            {'id': 89, 'width': 10, 'height': 4},
            {'id': 7, 'width': 1, 'height': 7}
        ]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertEqual(list, type(list_output))

    def test_one_rectangle(self):
        list_input = [
            {'id': 89, 'width': 10, 'height': 4},
        ]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertEqual(list_input, list_output)

    def test_two_rectangles(self):
        list_input = [
            {'id': 89, 'width': 10, 'height': 4},
            {'id': 7, 'width': 1, 'height': 7}
        ]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertEqual(list_input, list_output)

    def test_one_square(self):
        list_input = [
            {'id': 89, 'size': 4},
        ]
        json_list_input = Square.to_json_string(list_input)
        list_output = Square.from_json_string(json_list_input)
        self.assertEqual(list_input, list_output)

    def test_two_squares(self):
        list_input = [
            {'id': 89, 'size': 4},
            {'id': 7, 'size': 7}
        ]
        json_list_input = Square.to_json_string(list_input)
        list_output = Square.from_json_string(json_list_input)
        self.assertEqual(list_input, list_output)

    def test_empty(self):
        list_input = []
        json_list_input = Square.to_json_string(list_input)
        list_output = Square.from_json_string(json_list_input)
        self.assertEqual([], list_output)

    def test_empty(self):
        json_list_input = Square.to_json_string(None)
        list_output = Square.from_json_string(json_list_input)
        self.assertEqual([], list_output)

    def test_no_arg(self):
        with self.assertRaises(TypeError):
            json_list_input = Square.to_json_string()

    def test_two_arg(self):
        with self.assertRaises(TypeError):
            json_list_input = Square.to_json_string([], [])


class TestBase_Create(unittest.TestCase):
    """Runs tests for the create method of the Base class"""

    def test_rectangle(self):
        a = Rectangle(3, 5, 1)
        a_dictionary = a.to_dictionary()
        b = Rectangle.create(**a_dictionary)
        self.assertNotEqual(a, b)
        self.assertIsNot(a, b)

    def test_rectangle_str(self):
        a = Rectangle(3, 5, 1)
        a_dictionary = a.to_dictionary()
        b = Rectangle.create(**a_dictionary)
        self.assertEqual(str(b), str(a))

    def test_square(self):
        a = Square(3, 5, 1)
        a_dictionary = a.to_dictionary()
        b = Square.create(**a_dictionary)
        self.assertNotEqual(a, b)
        self.assertIsNot(a, b)

    def test_square_str(self):
        a = Square(3, 5, 1)
        a_dictionary = a.to_dictionary()
        b = Square.create(**a_dictionary)
        self.assertEqual(str(b), str(a))

    def test_not_kwargs(self):
        a = Square(3, 5, 1)
        a_dictionary = a.to_dictionary()
        with self.assertRaises(TypeError):
            b = Square.create(a_dictionary)


class TestBase_Load_From_File(unittest.TestCase):
    """Tests for the load_from_file method in the Base class"""
    @classmethod
    def tearDown(self):
        try:
            os.remove("Base.json")
        except IOError:
            pass
        try:
            os.remove("Rectangle.json")
        except IOError:
            pass
        try:
            os.remove("Square.json")
        except IOError:
            pass

    def test_one_rectangle(self):
        r1 = Rectangle(10, 7, 2, 8)
        list_rectangles_input = [r1]
        Rectangle.save_to_file(list_rectangles_input)
        list_rectangles_output = Rectangle.load_from_file()
        self.assertEqual(str(list_rectangles_output[0]), str(r1))
        self.assertEqual(list, type(list_rectangles_output))
        self.assertEqual(Rectangle, type(list_rectangles_output[0]))

    def test_two_rectangle(self):
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        list_rectangles_input = [r1, r2]
        Rectangle.save_to_file(list_rectangles_input)
        list_rectangles_output = Rectangle.load_from_file()
        self.assertEqual(str(list_rectangles_output[0]), str(r1))
        self.assertEqual(str(list_rectangles_output[1]), str(r2))
        self.assertEqual(list, type(list_rectangles_output))
        for x in list_rectangles_output:
            self.assertEqual(Rectangle, type(x))

    def test_square(self):
        s1 = Square(5)
        list_squares_input = [s1]
        Square.save_to_file(list_squares_input)
        list_squares_output = Square.load_from_file()
        self.assertEqual(str(list_squares_output[0]), str(s1))
        self.assertEqual(list, type(list_squares_output))
        self.assertEqual(Square, type(list_squares_output[0]))

    def test_two_squares(self):
        s1 = Square(7, 9, 1)
        s2 = Square(5)
        list_squares_input = [s1, s2]
        Square.save_to_file(list_squares_input)
        list_squares_output = Square.load_from_file()
        self.assertEqual(str(list_squares_output[0]), str(s1))
        self.assertEqual(str(list_squares_output[1]), str(s2))
        self.assertEqual(list, type(list_squares_output))
        for x in list_squares_output:
            self.assertEqual(Square, type(x))

    def test_no_file(self):
        empty_list = Base.load_from_file()
        self.assertEqual([], empty_list)

    def test_with_args(self):
        with self.assertRaises(TypeError):
            my_list = Base.load_from_file("sample.json")
