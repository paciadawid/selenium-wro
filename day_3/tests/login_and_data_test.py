import unittest

mail = "seleniumwroclaw@gmail.com"
password = "test1"

class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)


if __name__ == '__main__':
    unittest.main()
