from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from day_3.selectors.account_selectors import *
from day_3.config import *


class AccountPage:

    def __init__(self, driver):
        self.driver = driver

    def check_address(self):
        self.driver.find_element(*my_addresses_selector).click()
        WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(alert_selector)
        )
        self.driver.find_element(*my_account_selector).click()

    def check_credit_slips(self):
        self.driver.find_element(*credit_slips_selector).click()
        WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(alert_selector)
        )
        self.driver.find_element(*my_account_selector).click()
