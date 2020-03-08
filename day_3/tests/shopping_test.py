import unittest
from selenium import webdriver
from day_3.pages.search import SearchPage
from day_3.pages.summary import SummaryPage
from day_3.config import *
from hamcrest import *

class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        options = webdriver.ChromeOptions()
        #options.add_argument("--start-maximized")
        self.driver = webdriver.Chrome(options=options)
        self.driver.get(URL)
        self.search_page = SearchPage(self.driver)
        self.summary_page = SummaryPage(self.driver)

    def test_check_price(self):
        self.search_page.search("Printed Summer")
        self.search_page.add_to_cart()
        total_price = self.summary_page.get_total_price()
        assert_that(total_price, less_than(200))
        shipping_price = self.summary_page.get_shipping_price()
        assert_that(shipping_price, equal_to(2))

    def tearDown(self) -> None:
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
