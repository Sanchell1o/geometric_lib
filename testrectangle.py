import unittest
import rectangle
class RectangleTestCase(unittest.TestCase):
    def test_zero_mul(self):
        res = rectangle.area(10, 0)
        self.assertEqual(res, 0)

    def test_square_mul(self):
        res = rectangle.area(10, 10)
        self.assertEqual(res, 100)

    def test_zero_perimeter(self):
        res = rectangle.perimeter(0, 0)
        self.assertEqual(res, 0)

    def test_square_perimeter(self):
        res = rectangle.perimeter(10, 10)
        self.assertEqual(res, 40)

    def test_square_negative(self):
        res=rectangle.area(-10,-10)
        self.assertEqual(res,"error")