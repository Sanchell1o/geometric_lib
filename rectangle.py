import unittest


def area(a, b):
    """
   Возвращает площадь прямоугольника

       Параметры:
           a (int): одна из сторон прямоугольника
           b (int): вторая сторона прямоугольника

       Возвращаемое значение:
           a*b (int): произведение двух сторон
   """
    return a * b


def perimeter(a, b):
    """
   Возвращает периметр прямоугольника

       Параметры:
           a (int): одна из сторон прямоугольника
           b (int): вторая сторона прямоугольника

       Возвращаемое значение:
           (a + b)*2 (int): удвоенная сумма сторон
   """
    return 2 * a + 2 * b


class RectangleTestCase(unittest.TestCase):
    def test_zero_mul(self):
        res = area(10, 0)
        self.assertEqual(res, 0)

    def test_square_mul(self):
        res = area(10, 10)
        self.assertEqual(res, 100)

    def test_zero_perimeter(self):
        res = perimeter(0, 0)
        self.assertEqual(res, 0)

    def test_square_perimeter(self):
        res = perimeter(10, 10)
        self.assertEqual(res, 40)