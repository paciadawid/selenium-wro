import unittest
from hamcrest import *
from day_1.src.calculator_class import Calculator

class CalculatorTests(unittest.TestCase):

    def test_sample(self):
        assert_that(1, equal_to(1))


if __name__ == "__main__":
    unittest.main()
