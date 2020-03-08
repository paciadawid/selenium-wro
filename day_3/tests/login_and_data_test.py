import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MyTestCase(unittest.TestCase):

    mail = "seleniumwroclaw@gmail.com"
    password = "test1"
    login_button_selector = (By.CLASS_NAME, "login")
    email_selector = (By.ID, "email")
    password_selector = (By.ID, "passwd")
    submit_selector = (By.ID, "SubmitLogin")
    my_addresses_selector = (By.XPATH, "//*[@title='Addresses']")
    alert_selector = (By.CSS_SELECTOR, ".alert")
    credit_slips_selector = (By.CSS_SELECTOR, ".icon-ban-circle")
    my_account_selector = (By.CSS_SELECTOR, ".account")

    def setUp(self) -> None:
        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")
        self.driver = webdriver.Chrome(options=options)
        self.driver.get("http://automationpractice.com/index.php")

    def login(self):
        self.driver.find_element(*self.login_button_selector).click()
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.email_selector)
        ).send_keys(self.mail)
        self.driver.find_element(*self.password_selector).send_keys(self.password)
        self.driver.find_element(*self.submit_selector).click()

    def check_my_addresses(self):
        self.driver.find_element(*self.my_addresses_selector).click()
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.alert_selector)
        )
        self.driver.find_element(*self.my_account_selector).click()

    def check_credit_slips(self):
        self.driver.find_element(*self.credit_slips_selector).click()
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.alert_selector)
        )
        self.driver.find_element(*self.my_account_selector).click()

    def test_addresses(self):
        self.login()
        self.check_my_addresses()

    def test_credit_slips(self):
        self.login()
        self.check_credit_slips()

    def tearDown(self) -> None:
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
