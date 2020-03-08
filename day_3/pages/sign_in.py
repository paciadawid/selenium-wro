from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from day_3.selectors.sign_in_selectors import *
from day_3.config import *

class SignInPage:

    def __init__(self, driver):
        self.driver = driver

    def login(self, mail, password):
        self.driver.find_element(*login_button_selector).click()
        WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(email_selector)
        ).send_keys(mail)
        self.driver.find_element(*password_selector).send_keys(password)
        self.driver.find_element(*submit_selector).click()
