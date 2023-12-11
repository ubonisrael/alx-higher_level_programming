#!/usr/bin/python3
"""Contains tests for Rectangle class. """
import unittest
import io
import sys
from models.rectangle import Rectangle
from models.base import Base


class RectangleTest_Init(unittest.TestCase):
    """Contains tests for the init method of Rectangle class. """

    def test_rect_instance(self):
        self.assertIsInstance(Rectangle(1, 1), Base)

    def test_rect_subclass(self):
        self.assertTrue(issubclass(Rectangle, Base))

    def test_rect_ids(self):
        """Checks that the ids for the rects created are correct. """
        a = Rectangle(1, 1)
        b = Rectangle(2, 2)
        self.assertEqual(a.id, b.id - 1)

    def test_unique_ids(self):
        """Checks that the ids for the rects created are correct. """
        a = Rectangle(2, 2, 1, 1, 9)
        self.assertEqual(a.id, 9)

    def test_none_ids(self):
        """Checks that the ids for the rects created are correct. """
        a = Rectangle(2, 2, 0, 0, None)
        b = Rectangle(2, 3, 1, 1, None)
        self.assertEqual(b.id, a.id + 1)

    def test_no_args_plus_unique_ids(self):
        """Checks that the ids for the rects created are correct. """
        a = Rectangle(1, 2)
        b = Rectangle(2, 3, 0, 0, 12)
        c = Rectangle(1, 3)
        self.assertEqual(c.id, a.id + 1)
        self.assertEqual(b.id, 12)


class TestRectangle_Attributes(unittest.TestCase):
    """Runs checks for its attribute. """

    @classmethod
    def setUp(self):
        self.r = Rectangle(2, 4)

    @classmethod
    def tearDown(self):
        del self.r

    def test_width_getter(self):
        """Checks that getter and setter methos work as they should. """
        self.assertEqual(self.r.width, 2)

    def test_width_setter(self):
        """Checks that getter and setter methos work as they should. """
        self.r.width = 4
        self.assertEqual(self.r.width, 4)

    def test_string_width(self):
        """Tests whether the width input values are correct. """
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            self.r.width = '2'

    def test_bool_width(self):
        """Tests whether the width input values are correct. """
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            self.r.width = True

    def test_list_width(self):
        """Tests whether the width input values are correct. """
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            self.r.width = [1, 2]

    def test_tuple_width(self):
        """Tests whether the width input values are correct. """
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            self.r.width = (1,)

    def test_dict_width(self):
        """Tests whether the width input values are correct. """
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            self.r.width = {'diction': 1}

    def test_sets_width(self):
        """Tests whether the width input values are correct. """
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            self.r.width = {'sets', 'notsets'}

    def test_zero_width(self):
        """Tests whether the width input values are correct. """
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            self.r.width = 0

    def test_neg_width(self):
        """Tests whether the width input values are correct. """
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            self.r.width = -5

    def test_height_getter(self):
        """Checks that getter and setter methos work as they should. """
        self.assertEqual(self.r.height, 4)

    def test_height_setter(self):
        """Checks that getter and setter methos work as they should. """
        self.r.height = 8
        self.assertEqual(self.r.height, 8)

    def test_string_height(self):
        """Tests whether the height input values are correct. """
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            self.r.height = '2'

    def test_bool_height(self):
        """Tests whether the height input values are correct. """
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            self.r.height = True

    def test_list_height(self):
        """Tests whether the height input values are correct. """
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            self.r.height = [1, 2]

    def test_tuple_height(self):
        """Tests whether the height input values are correct. """
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            self.r.height = (1, 2)

    def test_dict_width(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            self.r.height = {'diction': 1}

    def test_sets_height(self):
        """Tests whether the height input values are correct. """
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            self.r.height = {1, 2}

    def test_zero_height(self):
        """Tests whether the height input values are correct. """
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            self.r.height = 0

    def test_neg_height(self):
        """Tests whether the height input values are correct. """
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            self.r.height = -5

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


class TestRectangle_Area(unittest.TestCase):
    """Tests the area method."""
    def test_area(self):
        r = Rectangle(2, 3)
        self.assertEqual(r.area(), 6)

    def test_changed_val(self):
        r = Rectangle(2, 3)
        r.width = 4
        r.height = 6
        self.assertEqual(24, r.area())

    def test_large_values(self):
        r = Rectangle(999999999, 999999999)
        self.assertEqual(r.area(), 999999998000000001)

    def test_area_args(self):
        with self.assertRaises(TypeError):
            print(Rectangle(2, 4).area(1))


class TestRectangle_Display(unittest.TestCase):
    """Tests for the display  and string method"""

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
            Rectangle(2, 4).display(1)

    def test_display_with_no_x_no_y(self):
        r = Rectangle(2, 2)
        capture = TestRectangle_Display.capture_stdout(r, 'display')
        self.assertEqual("##\n##\n", capture.getvalue())

    def test_display_with_x_no_y(self):
        r = Rectangle(2, 2, 1)
        capture = TestRectangle_Display.capture_stdout(r, 'display')
        self.assertEqual(" ##\n ##\n", capture.getvalue())

    def test_display_with_no_x_y(self):
        r = Rectangle(2, 2, 0, 1)
        capture = TestRectangle_Display.capture_stdout(r, 'display')
        self.assertEqual("\n##\n##\n", capture.getvalue())

    def test_display_with_x_y(self):
        r = Rectangle(2, 2, 1, 1)
        capture = TestRectangle_Display.capture_stdout(r, 'display')
        self.assertEqual("\n ##\n ##\n", capture.getvalue())

    def test_str(self):
        r = Rectangle(2, 2)
        str_format = "[{:s}] ({:d}) {:d}/{:d} - {:d}/{:d}\n".format(
            r.__class__.__name__, r.id, r.x, r.y, r.width, r.height)
        capture = TestRectangle_Display.capture_stdout(r, 'print')
        self.assertEqual(str_format, capture.getvalue())

    def test_str_arg(self):
        r = Rectangle(2, 2)
        with self.assertRaises(TypeError):
            r.__str__(1)


class TestRectangle_Update(unittest.TestCase):
    """Tests for the update method"""
    def setUp(self):
        self.r = Rectangle(1, 2)

    def tearDown(self):
        del self.r

    def test_one_arg(self):
        self.r.update(89)
        self.assertEqual(self.r.id, 89)

    def test_two_args(self):
        self.r.update(89, 2)
        self.assertEqual(self.r.id, 89)
        self.assertEqual(self.r.width, 2)

    def test_three_args(self):
        self.r.update(89, 2, 4)
        self.assertEqual(self.r.id, 89)
        self.assertEqual(self.r.width, 2)
        self.assertEqual(self.r.height, 4)

    def test_four_args(self):
        self.r.update(89, 2, 4, 1)
        self.assertEqual(self.r.id, 89)
        self.assertEqual(self.r.width, 2)
        self.assertEqual(self.r.height, 4)
        self.assertEqual(self.r.x, 1)

    def test_five_args(self):
        self.r.update(89, 2, 4, 1, 2)
        self.assertEqual(self.r.id, 89)
        self.assertEqual(self.r.width, 2)
        self.assertEqual(self.r.height, 4)
        self.assertEqual(self.r.x, 1)
        self.assertEqual(self.r.y, 2)

    def test_six_args(self):
        self.r.update(89, 2, 4, 1, 2, 6)
        self.assertEqual(self.r.id, 89)
        self.assertEqual(self.r.width, 2)
        self.assertEqual(self.r.height, 4)
        self.assertEqual(self.r.x, 1)
        self.assertEqual(self.r.y, 2)

    def test_invalid_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            self.r.update(89, '2')

    def test_zer_width(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            self.r.update(89, 0)

    def test_neg_width(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            self.r.update(89, -1)

    def test_invalid_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            self.r.update(89, 4, '42')

    def test_zer_height(self):
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            self.r.update(89, 4, 0)

    def test_neg_height(self):
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            self.r.update(89, 4, -1)

    def test_invalid_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            self.r.update(89, 4, 1, '9')

    def test_neg_x(self):
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            self.r.update(89, 4, 1, -5)

    def test_invalid_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            self.r.update(89, 4, 1, 2, '9')

    def test_neg_x(self):
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            self.r.update(89, 4, 1, 3, -5)

    def test_args_and_kwargs(self):
        self.r.update(89, 2, 4, 1, 2, id=1, width=4)
        self.assertEqual(self.r.id, 89)
        self.assertEqual(self.r.width, 2)
        self.assertEqual(self.r.height, 4)
        self.assertEqual(self.r.x, 1)
        self.assertEqual(self.r.y, 2)

    def test_no_args_and_kwargs_id(self):
        self.r.update(id=1)
        self.assertEqual(self.r.id, 1)

    def test_no_args_and_kwargs_width(self):
        self.r.update(width=10)
        self.assertEqual(self.r.width, 10)

    def test_no_args_and_kwargs_height(self):
        self.r.update(height=12)
        self.assertEqual(self.r.height, 12)

    def test_no_args_and_kwargs_x(self):
        self.r.update(x=5)
        self.assertEqual(self.r.x, 5)

    def test_no_args_and_kwargs_y(self):
        self.r.update(y=6)
        self.assertEqual(self.r.y, 6)

    def test_no_args_and_kwargs_all(self):
        self.r.update(x=3, id=1, y=7, height=9, width=4)
        self.assertEqual(self.r.id, 1)
        self.assertEqual(self.r.width, 4)
        self.assertEqual(self.r.height, 9)
        self.assertEqual(self.r.x, 3)
        self.assertEqual(self.r.y, 7)

    def test_invalid_width_kwargs(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            self.r.update(width='2')

    def test_zer_width_kwargs(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            self.r.update(width=0)

    def test_neg_width_kwargs(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            self.r.update(width=-1)

    def test_invalid_height_kwargs(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            self.r.update(height='42')

    def test_zer_height_kwargs(self):
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            self.r.update(height=0)

    def test_neg_height_kwargs(self):
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            self.r.update(height=-1)

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


class TestRectangle_toDictionary(unittest.TestCase):
    """Tests for the to_dictionary method"""
    def test_args(self):
        with self.assertRaises(TypeError):
            print(Rectangle(2, 4).to_dictionary('print'))

    def test_type(self):
        r = Rectangle(2, 3)
        rd = r.to_dictionary()
        self.assertTrue(type(rd) == dict)

    def test_output(self):
        r = Rectangle(2, 4, 0, 0, 97)
        rd = r.to_dictionary()
        my_dict = {'x': 0, 'y': 0, 'id': 97, 'width': 2, 'height': 4}
        self.assertDictEqual(rd, my_dict)

    def test_two_rects(self):
        r1 = Rectangle(4, 6)
        rd = r1.to_dictionary()
        r2 = Rectangle(2, 2)
        r2.update(**rd)
        self.assertNotEqual(r1, r2)
