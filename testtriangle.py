import unittest
import triangle
class TestTriangleFunctions(unittest.TestCase):

    def test_positive_area(self):
        res = triangle.area(4, 5)
        self.assertEqual(res, 10)

    def test_zero_area(self):
        res = triangle.area(0, 5)
        self.assertEqual(res, 0)

    def test_positive_perimeter(self):
        res = triangle.perimeter(3, 4, 5)
        self.assertEqual(res, 12)

    def test_zero_perimetr(self):
        res = triangle.perimeter(0, 0, 0)
        self.assertEqual(res, 0)
