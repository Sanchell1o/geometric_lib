import unittest


def area(a, h):
    '''
        Возвращает площадь треугольника с основанием a и высотой h.

            Параметры:
                a(int): основание треугольника
                h(int): высота проведенная к стороне h

            Возвращаемое значение:
                 a * h/2(int): площадь  треугольника
        '''
    return a * h / 2


def perimeter(a, b, c):
    '''
        Возвращает периметр треугольника со сторонами a b c.

            Параметры:
                a(int): первая сторона треугольника
                b(int): вторая сторона треугольника
                b(int): третья сторона треугольника

            Возвращаемое значение:
                a + b + с: периметр треугольника
    '''
    return a + b + c


class TestTriangleFunctions(unittest.TestCase):

    def test_positive_area(self):
        res = area(4, 5)
        self.assertEqual(res, 10)

    def test_zero_area(self):
        res = area(0, 5)
        self.assertEqual(res, 0)

    def test_positive_perimeter(self):
        res = perimeter(3, 4, 5)
        self.assertEqual(res, 12)

    def test_zero_perimetr(self):
        res = perimeter(0, 0, 0)
        self.assertEqual(res, 0)

