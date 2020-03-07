from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
driver = webdriver.Chrome(options=options)
driver.get("http://automationpractice.com/index.php")

logo = driver.find_element_by_css_selector(".logo")
cart_button = driver.find_element_by_css_selector(".shopping_cart")
newsletter_field = driver.find_element_by_css_selector("#newsletter-input")
twitter_button = driver.find_element_by_css_selector(".twitter")
popular_button = driver.find_element_by_css_selector(".active#homefeatured")
contact_us_button = driver.find_element_by_css_selector("#contact-link a")

driver.quit()
