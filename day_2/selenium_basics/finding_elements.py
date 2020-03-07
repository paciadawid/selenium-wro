from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
driver = webdriver.Chrome(options=options)
driver.get("http://automationpractice.com/index.php")

logo = driver.find_element_by_id("header_logo")
cart_button = driver.find_element_by_class_name("shopping_cart")
newsletter_field = driver.find_element_by_id("newsletter-input")
twitter_button = driver.find_element_by_class_name("twitter")
popular_button = driver.find_element_by_class_name("homefeatured")
contact_us_button = driver.find_element_by_id("contact-link")

driver.quit()
