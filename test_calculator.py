import unittest

from calculator import plus, minus, divide, multiplication, calculator


class CalculatorTest(unittest.TestCase):


    def test_plus(self):
        self.assertEqual(plus(1, 2), 3)

    def test_plus_negative(self):
        self.assertEqual(plus(-1, 2), 1)
    
    def test_plus_float(self):
        self.assertAlmostEqual(plus(1.1, 2), 3.1)

    def test_plus_zero(self):
        self.assertEqual(plus(5, 0), 5)



    def test_minus(self):
        self.assertEqual(minus(3, 1), 2)

    def test_minus_negative(self):
        self.assertEqual(minus(-3, 1), -4)

    def test_minus_zero(self):
        self.assertEqual(minus(0, 5), -5)



    def test_divide(self):
        self.assertEqual(divide(4, 2), 2)

    def test_divide_negative(self):
        self.assertEqual(divide(-4, 2), -2)

    def test_divide_two_negative(self):
        self.assertEqual(divide(-4, -2), 2)

    def test_divide_float(self):
        self.assertAlmostEqual(divide(7, 2), 3.5)

    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            divide(5, 0)



    def test_multiplication(self):
        self.assertEqual(multiplication(4, 2), 8)

    def test_multiplication_zero(self):
        self.assertEqual(multiplication(100,0),0)

    def test_multiplication_two_negative(self):
        self.assertEqual(multiplication(-5, -4), 20)


if __name__ == "__main__":
    calculator()