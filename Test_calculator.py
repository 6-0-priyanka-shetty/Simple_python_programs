import unittest
from math_utils import add,divide

class TestCalculator(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2,3),5)

    def test_divide(self):
        self.assertEqual(divide(10,2),5)

    def test_valueError(self):
        with self.assertRaises(ValueError):
            a=int('four')

    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            divide(10,0)


if __name__=="__main__":
    unittest.main()