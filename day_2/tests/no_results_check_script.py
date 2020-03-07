from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
driver = webdriver.Chrome(options=options)
driver.get("http://automationpractice.com/index.php")

search_field_selector = (By.ID, "search_query_top")
search_button_selector = (By.NAME, "submit_search")
error_box_selector = (By.CSS_SELECTOR, ".alert")

driver.find_element(*search_field_selector).send_keys("test")
driver.find_element(*search_button_selector).click()

# 1 option
driver.find_element(*error_box_selector)

# 2 option
WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located(error_box_selector)
)

driver.quit()
