from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
driver = webdriver.Chrome(options=options)
driver.get("http://automationpractice.com/index.php")

logo = driver.find_element_by_xpath("//*[contains(@class, 'logo')]")
cart_button = driver.find_element_by_xpath("//*[@class='shopping_cart']")
newsletter_field = driver.find_element_by_xpath("//*[@id='newsletter-input']")
twitter_button = driver.find_element_by_xpath("//*[@class='twitter']")
popular_button = driver.find_element_by_xpath("//*[@href='#homefeatured']")
contact_us_button = driver.find_element_by_xpath("//*[@id='contact-link']/a")

driver.quit()
