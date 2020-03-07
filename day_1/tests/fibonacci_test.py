import unittest
from day_1.src.fibonacci import fibonacci_1
from hamcrest import *


class MyTestCase(unittest.TestCase):

    def test_positive(self):
        assert_that(fibonacci_1(10), equal_to(34))

    def test_zero(self):
        assert_that(fibonacci_1(0), equal_to(False))

    def test_negative(self):
        assert_that(fibonacci_1(-1), equal_to(False))

    def test_string(self):
        assert_that(fibonacci_1("xxx"), equal_to(False))


if __name__ == '__main__':
    unittest.main()
