import math
import unittest


def area(r):
    '''
    Возвращает площадь окружности радиусом r.

        Параметры:
            r(int): радиус окружности

        Возвращаемое значение:
             math.pi * r * r(int): площадь окружности
    '''
    return math.pi * r * r


def perimeter(r):
    '''
    Возвращает периметр окружности радиусом r.

        Параметры:
            r(int): радиус окружности

        Возвращаемое значение:
             2 * math.pi * r(int): периметр окружности
    '''
    return 2 * math.pi * r


class TestCircle(unittest.TestCase):
    def test_positive_area(self):
        res = area(5)
        self.assertAlmostEqual(res, 78.53981633974483)

    def test_zero_area(self):
        res = area(0)
        self.assertAlmostEqual(res, 0)

    def test_positive_perimeter(self):
        res = perimeter(5)
        self.assertAlmostEqual(res, 31.41592653589793)

    def test_zero_perimeter(self):
        res = perimeter(0)
        self.assertAlmostEqual(res, 0)
