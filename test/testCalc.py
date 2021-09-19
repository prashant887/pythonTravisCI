import sys


from src.Calculator import Calculator
import unittest


class TestArithmeticOperations(unittest.TestCase):

    def setUp(self):
        self.arith = Calculator(6,4)

    def test_addition(self):
        self.assertEqual(self.arith.add(), 10)


if __name__ == "__main__":
    unittest.main()