#!/usr/bin/python3
"""Contains tests for Rectangle class. """
import unittest
from models.rectangle import Rectangle
from models.base import Base


class RectangleTest(unittest.TestCase):
    """Contains tests for Rectangle class. """

    @classmethod
    def setUpClass(cls):
        """Sets up rectangle instances for testing. """
        cls.rect1 = Rectangle(10, 2)
        cls.rect2 = Rectangle(2, 10)
        cls.rect3 = Rectangle(4, 5, 0, 0, 7)
        cls.rect4 = Rectangle(8, 9, 1, 2)

    @classmethod
    def tearDownClass(cls):
        """Deletes instances that had been created for testing."""
        del cls.rect1
        del cls.rect2
        del cls.rect3
        del cls.rect4

    def test_rect_ids(self):
        """Checks that the ids for the rects created are correct. """
        self.assertEqual(RectangleTest.rect1.id, 1)
        self.assertEqual(RectangleTest.rect2.id, 2)
        self.assertEqual(RectangleTest.rect3.id, 7)
        self.assertEqual(RectangleTest.rect4.id, 3)

    def test_rect_props(self):
        """Checks the class properties of rectangle objects. """
        self.assertIsInstance(RectangleTest.rect1, Rectangle)
        self.assertIsInstance(RectangleTest.rect1, Base)
        self.assertIs(type(RectangleTest.rect1), Rectangle)
        self.assertIsNot(type(RectangleTest.rect1), Base)

    def test_rect_getters(self):
        """Checks that getter and setter methos work as they should. """
        self.assertEqual(RectangleTest.rect4.width, 8)
        self.assertEqual(RectangleTest.rect4.height, 9)
        self.assertEqual(RectangleTest.rect4.x, 1)
        self.assertEqual(RectangleTest.rect4.y, 2)

        RectangleTest.rect4.width = 10
        RectangleTest.rect4.height = 12
        RectangleTest.rect4.x = 2
        RectangleTest.rect4.y = 0

        self.assertEqual(RectangleTest.rect4.width, 10)
        self.assertEqual(RectangleTest.rect4.height, 12)
        self.assertEqual(RectangleTest.rect4.x, 2)
        self.assertEqual(RectangleTest.rect4.y, 0)

    def test_rect_width(self):
        """Tests whether the width input values are correct. """
        with self.assertRaises(TypeError):
            RectangleTest.rect2.width = '2'
        with self.assertRaises(TypeError):
            RectangleTest.rect2.width = True
        with self.assertRaises(TypeError):
            RectangleTest.rect2.width = [1, 2]
        with self.assertRaises(TypeError):
            RectangleTest.rect2.width = (1,)
        with self.assertRaises(TypeError):
            RectangleTest.rect2.width = {'diction': 1}
        with self.assertRaises(TypeError):
            RectangleTest.rect2.width = {'sets', 'notsets'}
        with self.assertRaises(ValueError):
            RectangleTest.rect2.width = 0
        with self.assertRaises(ValueError):
            RectangleTest.rect2.width = -5

    def test_rect_height(self):
        """Tests whether the height input values are correct. """
        with self.assertRaises(TypeError):
            RectangleTest.rect2.height = '2'
        with self.assertRaises(TypeError):
            RectangleTest.rect2.height = True
        with self.assertRaises(TypeError):
            RectangleTest.rect2.height = [1, 2]
        with self.assertRaises(TypeError):
            RectangleTest.rect2.height = (1,)
        with self.assertRaises(TypeError):
            RectangleTest.rect2.height = {'diction': 1}
        with self.assertRaises(TypeError):
            RectangleTest.rect2.height = {'sets', 'notsets'}
        with self.assertRaises(ValueError):
            RectangleTest.rect2.height = 0
        with self.assertRaises(ValueError):
            RectangleTest.rect2.height = -5

    def test_rect_x(self):
        """Tests whether the x input values are correct. """
        with self.assertRaises(TypeError):
            RectangleTest.rect2.x = '2'
        with self.assertRaises(TypeError):
            RectangleTest.rect2.x = True
        with self.assertRaises(TypeError):
            RectangleTest.rect2.x = [1, 2]
        with self.assertRaises(TypeError):
            RectangleTest.rect2.x = (1,)
        with self.assertRaises(TypeError):
            RectangleTest.rect2.x = {'diction': 1}
        with self.assertRaises(TypeError):
            RectangleTest.rect2.x = {'sets', 'notsets'}
        with self.assertRaises(ValueError):
            RectangleTest.rect2.x = -5

    def test_rect_y(self):
        """Tests whether the x input values are correct. """
        with self.assertRaises(TypeError):
            RectangleTest.rect2.y = '2'
        with self.assertRaises(TypeError):
            RectangleTest.rect2.y = True
        with self.assertRaises(TypeError):
            RectangleTest.rect2.y = [1, 2]
        with self.assertRaises(TypeError):
            RectangleTest.rect2.y = (1,)
        with self.assertRaises(TypeError):
            RectangleTest.rect2.y = {'diction': 1}
        with self.assertRaises(TypeError):
            RectangleTest.rect2.y = {'sets', 'notsets'}
        with self.assertRaises(ValueError):
            RectangleTest.rect2.y = -5

    def test_rect_area(self):
        """Tests whether the area returns the expected output."""
        self.assertEqual(RectangleTest.rect4.area(), 72)
        self.assertEqual(RectangleTest.rect1.area(), 20)

    def test_rect_update(self):
        """Checks the update method for args. """
        RectangleTest.rect1.update(89)
        self.assertEqual(RectangleTest.rect1.id, 89)

        RectangleTest.rect1.update(89, 2)
        self.assertEqual(RectangleTest.rect1.id, 89)
        self.assertEqual(RectangleTest.rect1.width, 2)

        RectangleTest.rect1.update(89, 2, 3)
        self.assertEqual(RectangleTest.rect1.id, 89)
        self.assertEqual(RectangleTest.rect1.width, 2)
        self.assertEqual(RectangleTest.rect1.height, 3)

        RectangleTest.rect1.update(89, 2, 3, 4)
        self.assertEqual(RectangleTest.rect1.id, 89)
        self.assertEqual(RectangleTest.rect1.width, 2)
        self.assertEqual(RectangleTest.rect1.height, 3)
        self.assertEqual(RectangleTest.rect1.x, 4)

        RectangleTest.rect1.update(89, 2, 3, 4, 5)
        self.assertEqual(RectangleTest.rect1.id, 89)
        self.assertEqual(RectangleTest.rect1.width, 2)
        self.assertEqual(RectangleTest.rect1.height, 3)
        self.assertEqual(RectangleTest.rect1.x, 4)
        self.assertEqual(RectangleTest.rect1.y, 5)

    def test_update_kwargs(self):
        """Tests the update method for kwargs."""
        RectangleTest.rect1.update(89, 2, 3, 4, 5, id=1, width=3, x=4)
        self.assertEqual(RectangleTest.rect1.id, 89)
        self.assertEqual(RectangleTest.rect1.width, 2)
        self.assertEqual(RectangleTest.rect1.height, 3)
        self.assertEqual(RectangleTest.rect1.x, 4)
        self.assertEqual(RectangleTest.rect1.y, 5)

        RectangleTest.rect1.update(id=109, width=5, x=1, height=10, y=0)
        self.assertEqual(RectangleTest.rect1.id, 109)
        self.assertEqual(RectangleTest.rect1.width, 5)
        self.assertEqual(RectangleTest.rect1.height, 10)
        self.assertEqual(RectangleTest.rect1.x, 1)
        self.assertEqual(RectangleTest.rect1.y, 0)
