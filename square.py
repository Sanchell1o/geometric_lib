import unittest


def area(a):
    '''
       Возвращает площадь квадрата со стороной а.

           Параметры:
               а(int): сторона квадрата

           Возвращаемое значение:
                a*a(int): площадь квадрата
       '''
    return a * a


def perimeter(a):
    '''
        Возвращает периметр квадрата со стороной a.

            Параметры:
                a(int): сторона квадрата.

            Возвращаемое значение:
                4*а(int): периметр квадрата.
        '''
    return 4 * a


class SquareTestCase(unittest.TestCase):
    def test_zero_area(self):
        res = area(0)
        self.assertEqual(res, 0)

    def test_positive_area(self):
        res = area(10)
        self.assertEqual(res, 100)

    def test_zero_perimeter(self):
        res = perimeter(0)
        self.assertEqual(res, 0)

    def test_positive_perimeter(self):
        res = perimeter(10)
        self.assertEqual(res, 40)
