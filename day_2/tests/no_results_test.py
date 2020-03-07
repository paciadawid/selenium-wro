import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MyTestCase(unittest.TestCase):

    search_field_selector = (By.ID, "search_query_top")
    search_button_selector = (By.NAME, "submit_search")
    error_box_selector = (By.CSS_SELECTOR, ".alert")

    def setUp(self) -> None:
        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")
        self.driver = webdriver.Chrome(options=options)
        self.driver.get("http://automationpractice.com/index.php")

    def test_no_results(self):
        self.driver.find_element(*self.search_field_selector).send_keys("test")
        self.driver.find_element(*self.search_button_selector).click()

        # 1 option
        self.driver.find_element(*self.error_box_selector)

        # 2 option
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.error_box_selector)
        )

    def tearDown(self) -> None:
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
