import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = SimpleCalculator()

    def test_addition(self):
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(10, 15), 25)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(-5, -3), -8)

        self.assertEqual(self.calc.add(0, 5), 5)
        self.assertEqual(self.calc.add(7, 0), 7)

        self.assertEqual(self.calc.add(2.5, 3.5), 6.0)
        self.assertEqual(self.calc.add(1.1, 2.2), 3.3)

    def test_subtraction(self):
        self.assertEqual(self.calc.subtract(5, 3), 2)
        self.assertEqual(self.calc.subtract(10, 15), -5)

        self.assertEqual(self.calc.subtract(-1, 1), -2)
        self.assertEqual(self.calc.subtract(-5, -3), -2)

        self.assertEqual(self.calc.subtract(0, 5), -5)
        self.assertEqual(self.calc.subtract(7, 0), 7)

        self.assertEqual(self.calc.subtract(5.5, 3.5), 2.0)  # Fixed
        self.assertEqual(self.calc.subtract(3.3, 1.1), 2.2)

    def test_multiplication(self):
        self.assertEqual(self.calc.multiply(2, 3), 6)
        self.assertEqual(self.calc.multiply(5, 4), 20)

        self.assertEqual(self.calc.multiply(-2, 3), -6)
        self.assertEqual(self.calc.multiply(-2, -3), 6)

        self.assertEqual(self.calc.multiply(0, 5), 0)
        self.assertEqual(self.calc.multiply(7, 0), 0)

        self.assertEqual(self.calc.multiply(2.5, 4), 10.0)  # Fixed
        self.assertEqual(self.calc.multiply(1.5, 2.5), 3.75)

    def test_division(self):
        self.assertEqual(self.calc.divide(10, 2), 5)
        self.assertEqual(self.calc.divide(9, 3), 3)

        self.assertEqual(self.calc.divide(5, 2), 2.5)  # Fixed
        self.assertEqual(self.calc.divide(1, 4), 0.25)

        self.assertEqual(self.calc.divide(-10, 2), -5)
        self.assertEqual(self.calc.divide(10, -2), -5)  # Fixed
        self.assertEqual(self.calc.divide(-10, -2), 5)  # Fixed

        self.assertIsNone(self.calc.divide(10, 0))      # Fixed
        self.assertIsNone(self.calc.divide(0, 0))       # Fixed
        self.assertIsNone(self.calc.divide(-5, 0))      # Fixed

        self.assertEqual(self.calc.divide(0, 5), 0)

if __name__ == '__main__':
    unittest.main()





