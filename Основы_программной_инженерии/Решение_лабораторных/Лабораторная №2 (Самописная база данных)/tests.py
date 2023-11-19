class Calculator:
    def __init__(self):
        pass

    def add(self, x1, x2):
        return x1 + x2

    def multiply(self, x1, x2):
        return x1 * x2


import unittest
class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calculator = Calculator()
    def test_functions_calculator(self):
        add = self.calculator.add(4,18)
        multiply = self.calculator.multiply(add, 2)
        self.assertEqual(multiply, 44)