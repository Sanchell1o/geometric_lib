import unittest
import square
class SquareTestCase(unittest.TestCase):
    def test_zero_area(self):
        res = square.area(0)
        self.assertEqual(res, 0)

    def test_positive_area(self):
        res = square.area(10)
        self.assertEqual(res, 100)

    def test_zero_perimeter(self):
        res = square.perimeter(0)
        self.assertEqual(res, 0)

    def test_positive_perimeter(self):
        res = square.perimeter(10)
        self.assertEqual(res, 40)
