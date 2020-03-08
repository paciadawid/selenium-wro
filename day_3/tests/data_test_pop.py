import unittest
from selenium import webdriver
from day_3.pages.sign_in import SignInPage
from day_3.pages.account import AccountPage
from day_3.config import *


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")
        self.driver = webdriver.Chrome(options=options)
        self.driver.get(URL)
        self.sign_in_page = SignInPage(self.driver)
        self.account_page = AccountPage(self.driver)

    def test_account_data(self):
        self.sign_in_page.login(mail, password)
        self.account_page.check_address()
        self.account_page.check_credit_slips()

    def tearDown(self) -> None:
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
