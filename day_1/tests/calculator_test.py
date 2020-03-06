import unittest
from hamcrest import *
from day_1.src.calculator_class import Calculator


class CalculatorTests(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_zero_division(self):
        assert_that(self.calc.div(1, 0), equal_to(False))

    def test_string(self):
        assert_that(self.calc.add(1, "1"), equal_to(False))

    def test_float(self):
        assert_that(self.calc.add(1, 1.0), equal_to(2.0))

    def test_mul(self):
        assert_that(self.calc.mul(-1, -1), equal_to(1))

    def tearDown(self):
        pass

if __name__ == "__main__":
    unittest.main()
