from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
driver = webdriver.Chrome(options=options)
driver.get("http://automationpractice.com/index.php")

search_field_locator = (By.ID, "search_query_top")

WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located(search_field_locator)
).send_keys('test')

#search_field.send_keys("test")

driver.quit()
