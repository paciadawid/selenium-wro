from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from day_3.selectors.summary_selectors import *
from day_3.config import *

class SummaryPage:

    def __init__(self, driver):
        self.driver = driver

    def get_total_price(self):
        #total_price_element = self.driver.find_element(*total_price_selector)
        total_price_element = WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(total_price_selector)
        )
        price = total_price_element.text
        return float(price[1:])

    def get_shipping_price(self):
        shipping_price_element = self.driver.find_element(*shipping_price_selector)
        price = shipping_price_element.text
        return float(price[1:])

