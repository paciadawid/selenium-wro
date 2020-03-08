from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from day_3.selectors.search_selectors import *
from day_3.config import *

class SearchPage:

    def __init__(self, driver):
        self.driver = driver

    def search(self, search_text):
        self.driver.find_element(*input_search_selector).send_keys(search_text)
        self.driver.find_element(*loop_selector).click()

    def add_to_cart(self):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(add_to_cart_selector)
        ).click()
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(proceed_to_checkout_selector)
        ).click()
