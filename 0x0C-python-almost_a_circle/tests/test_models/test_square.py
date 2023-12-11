#!/usr/bin/python3
"""Contains tests for Square class. """
import unittest
import io
import sys
from models.square import Square
from models.rectangle import Rectangle
from models.base import Base


class SquareTest_Init(unittest.TestCase):
    """Contains tests for the init method of Square class. """

    def test_square_instance_base(self):
        self.assertIsInstance(Square(1), Base)

    def test_square_instance_rect(self):
        self.assertIsInstance(Square(1), Rectangle)

    def testsubclass_base(self):
        self.assertTrue(issubclass(Square, Base))

    def testsubclass_rect(self):
        self.assertTrue(issubclass(Square, Rectangle))

    def test_ids(self):
        """Checks that the ids for the rects created are correct. """
        a = Square(1)
        b = Square(2)
        self.assertEqual(a.id, b.id - 1)

    def test_unique_ids(self):
        """Checks that the ids for the rects created are correct. """
        a = Square(2, 1, 1, 9)
        self.assertEqual(a.id, 9)

    def test_none_ids(self):
        """Checks that the ids for the rects created are correct. """
        a = Square(2, 0, 0, None)
        b = Square(2, 1, 1, None)
        self.assertEqual(b.id, a.id + 1)

    def test_no_args_plus_unique_ids(self):
        """Checks that the ids for the rects created are correct. """
        a = Square(1)
        b = Square(2, 0, 0, 12)
        c = Square(1)
        self.assertEqual(c.id, a.id + 1)
        self.assertEqual(b.id, 12)


class TestSquare_Attributes(unittest.TestCase):
    """Runs checks for its attribute. """

    @classmethod
    def setUp(self):
        self.r = Square(4)

    @classmethod
    def tearDown(self):
        del self.r

    def test_size_getter(self):
        """Checks that getter and setter methos work as they should. """
        self.assertEqual(self.r.size, 4)

    def test_size_setter(self):
        """Checks that getter and setter methos work as they should. """
        self.r.width = 4
        self.assertEqual(self.r.size, 4)

    def test_string_size(self):
        """Tests whether the width input values are correct. """
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            self.r.size = '2'

    def test_bool_size(self):
        """Tests whether the width input values are correct. """
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            self.r.size = True

    def test_list_size(self):
        """Tests whether the width input values are correct. """
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            self.r.size = [1, 2]

    def test_tuple_size(self):
        """Tests whether the width input values are correct. """
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            self.r.size = (1,)

    def test_dict_size(self):
        """Tests whether the width input values are correct. """
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            self.r.size = {'diction': 1}

    def test_sets_size(self):
        """Tests whether the width input values are correct. """
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            self.r.size = {'sets', 'notsets'}

    def test_zero_size(self):
        """Tests whether the width input values are correct. """
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            self.r.size = 0

    def test_neg_size(self):
        """Tests whether the width input values are correct. """
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            self.r.size = -5

    def test_x_getter(self):
        """Checks that getter and setter methos work as they should. """
        self.assertEqual(self.r.x, 0)

    def test_x_setter(self):
        """Checks that getter and setter methos work as they should. """
        self.r.x = 1
        self.assertEqual(self.r.x, 1)

    def test_string_x(self):
        """Tests whether the x input values are correct. """
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            self.r.x = '2'

    def test_sets_x(self):
        """Tests whether the x input values are correct. """
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            self.r.x = {'2', '1'}

    def test_dict_x(self):
        """Tests whether the x input values are correct. """
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            self.r.x = {'def': 1}

    def test_tuple_x(self):
        """Tests whether the x input values are correct. """
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            self.r.x = (1, 3)

    def test_list_x(self):
        """Tests whether the x input values are correct. """
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            self.r.x = [2]

    def test_bool_x(self):
        """Tests whether the x input values are correct. """
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            self.r.x = True

    def test_neg_x(self):
        """Tests whether the x input values are correct. """
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            self.r.x = -1

    def test_y_getter(self):
        """Checks that getter and setter methos work as they should. """
        self.assertEqual(self.r.y, 0)

    def test_y_setter(self):
        """Checks that getter and setter methos work as they should. """
        self.r.y = 2
        self.assertEqual(self.r.y, 2)

    def test_string_y(self):
        """Tests whether the y input values are correct. """
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            self.r.y = '2'

    def test_bool_y(self):
        """Tests whether the y input values are correct. """
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            self.r.y = False

    def test_list_y(self):
        """Tests whether the y input values are correct. """
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            self.r.y = [1]

    def test_dict_y(self):
        """Tests whether the y input values are correct. """
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            self.r.y = {'sed': 2}

    def test_set_y(self):
        """Tests whether the y input values are correct. """
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            self.r.y = {1, 2}

    def test_tuple_y(self):
        """Tests whether the y input values are correct. """
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            self.r.y = (1, 2)

    def test_neg_y(self):
        """Tests whether the y input values are correct. """
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            self.r.y = -1


class TestSquare_Area(unittest.TestCase):
    """Tests the area method."""
    def test_area(self):
        r = Square(2)
        self.assertEqual(r.area(), 4)

    def test_changed_val(self):
        r = Square(3)
        r.size = 4
        self.assertEqual(16, r.area())

    def test_large_values(self):
        r = Square(999999999)
        self.assertEqual(r.area(), 999999998000000001)

    def test_area_args(self):
        with self.assertRaises(TypeError):
            print(Square(2).area(1))


class TestSquare_Display(unittest.TestCase):
    """Tests for the display and string method"""

    @staticmethod
    def capture_stdout(rect, method):
        """Captures and returns text printed to stdout"""
        capture = io.StringIO()
        sys.stdout = capture
        if method == 'print':
            print(rect)
        else:
            rect.display()
        sys.stdout = sys.__stdout__
        return capture

    def test_display_with_args(self):
        with self.assertRaises(TypeError):
            Square(2).display(1)

    def test_display_with_no_x_no_y(self):
        r = Square(2)
        capture = TestSquare_Display.capture_stdout(r, 'display')
        self.assertEqual("##\n##\n", capture.getvalue())

    def test_display_with_x_no_y(self):
        r = Square(2, 2)
        capture = TestSquare_Display.capture_stdout(r, 'display')
        self.assertEqual("  ##\n  ##\n", capture.getvalue())

    def test_display_with_no_x_y(self):
        r = Square(2, 0, 1)
        capture = TestSquare_Display.capture_stdout(r, 'display')
        self.assertEqual("\n##\n##\n", capture.getvalue())

    def test_display_with_x_y(self):
        r = Square(2, 1, 1)
        capture = TestSquare_Display.capture_stdout(r, 'display')
        self.assertEqual("\n ##\n ##\n", capture.getvalue())

    def test_str(self):
        r = Square(2)
        str_format = "[{:s}] ({:d}) {:d}/{:d} - {:d}\n".format(
            r.__class__.__name__, r.id, r.x, r.y, r.size)
        capture = TestSquare_Display.capture_stdout(r, 'print')
        self.assertEqual(str_format, capture.getvalue())

    def test_str_arg(self):
        r = Square(2)
        with self.assertRaises(TypeError):
            r.__str__(1)


class TestSquare_Update(unittest.TestCase):
    """Tests for the update method"""
    def setUp(self):
        self.r = Square(3)

    def tearDown(self):
        del self.r

    def test_one_arg(self):
        self.r.update(89)
        self.assertEqual(self.r.id, 89)

    def test_two_args(self):
        self.r.update(89, 2)
        self.assertEqual(self.r.id, 89)
        self.assertEqual(self.r.size, 2)

    def test_three_args(self):
        self.r.update(89, 2, 4)
        self.assertEqual(self.r.id, 89)
        self.assertEqual(self.r.size, 2)
        self.assertEqual(self.r.x, 4)

    def test_four_args(self):
        self.r.update(89, 2, 4, 1)
        self.assertEqual(self.r.id, 89)
        self.assertEqual(self.r.size, 2)
        self.assertEqual(self.r.x, 4)
        self.assertEqual(self.r.y, 1)

    def test_five_args(self):
        self.r.update(89, 2, 4, 1, 2)
        self.assertEqual(self.r.id, 89)
        self.assertEqual(self.r.size, 2)
        self.assertEqual(self.r.x, 4)
        self.assertEqual(self.r.y, 1)

    def test_invalid_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            self.r.update(89, '2')

    def test_zer_size(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            self.r.update(89, 0)

    def test_neg_size(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            self.r.update(89, -1)

    def test_invalid_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            self.r.update(89, 1, '9')

    def test_neg_x(self):
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            self.r.update(89, 1, -5)

    def test_invalid_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            self.r.update(89, 1, 2, '9')

    def test_neg_y(self):
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            self.r.update(89, 1, 3, -5)

    def test_args_and_kwargs(self):
        self.r.update(89, 2, 1, 2, id=1, width=4)
        self.assertEqual(self.r.id, 89)
        self.assertEqual(self.r.size, 2)
        self.assertEqual(self.r.x, 1)
        self.assertEqual(self.r.y, 2)

    def test_no_args_and_kwargs_id(self):
        self.r.update(id=1)
        self.assertEqual(self.r.id, 1)

    def test_no_args_and_kwargs_width(self):
        self.r.update(size=10)
        self.assertEqual(self.r.size, 10)

    def test_no_args_and_kwargs_x(self):
        self.r.update(x=5)
        self.assertEqual(self.r.x, 5)

    def test_no_args_and_kwargs_y(self):
        self.r.update(y=6)
        self.assertEqual(self.r.y, 6)

    def test_no_args_and_kwargs_all(self):
        self.r.update(x=3, id=1, y=7, size=4)
        self.assertEqual(self.r.id, 1)
        self.assertEqual(self.r.size, 4)
        self.assertEqual(self.r.x, 3)
        self.assertEqual(self.r.y, 7)

    def test_invalid_size_kwargs(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            self.r.update(size='2')

    def test_zer_size_kwargs(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            self.r.update(size=0)

    def test_neg_size_kwargs(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            self.r.update(size=-1)

    def test_invalid_x_kwargs(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            self.r.update(x='9')

    def test_neg_x_kwargs(self):
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            self.r.update(x=-5)

    def test_invalid_y_kwargs(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            self.r.update(y='9')

    def test_neg_x_kwargs(self):
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            self.r.update(y=-5)


class TestSquare_toDictionary(unittest.TestCase):
    """Tests for the to_dictionary method"""
    def test_args(self):
        with self.assertRaises(TypeError):
            print(Square(2, 4).to_dictionary('print'))

    def test_type(self):
        r = Square(2, 3)
        rd = r.to_dictionary()
        self.assertTrue(type(rd) == dict)

    def test_output(self):
        r = Square(2, 0, 0, 97)
        rd = r.to_dictionary()
        my_dict = {'x': 0, 'y': 0, 'id': 97, 'size': 2}
        self.assertDictEqual(rd, my_dict)

    def test_two_rects(self):
        r1 = Square(4, 6)
        rd = r1.to_dictionary()
        r2 = Square(2, 2)
        r2.update(**rd)
        self.assertNotEqual(r1, r2)
