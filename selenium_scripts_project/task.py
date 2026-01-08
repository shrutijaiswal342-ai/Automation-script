from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://www.amazon.in")
driver.maximize_window()
time.sleep(5)  

#  Assertion  Home page opened
assert "amazon" in driver.current_url.lower()

# Search code assertion #
search_field = driver.find_element(By.ID, "twotabsearchtextbox")
assert search_field.is_displayed(), "Search box not visible"

search_field.send_keys("samsung mobile")
search_btn = driver.find_element(By.ID, "nav-search-submit-text")
search_btn.click()
time.sleep(3)

# assert  Search result page loaded #
assert "samsung" in driver.page_source.lower(), "Search results not loaded"


driver.execute_script("window.scrollBy(0, 300);")

#  brand filter  code #
brand = driver.find_element(By.XPATH, "//span[text()='Samsung']")
brand.click()
time.sleep(4)

# Assertion Storage filter applied   #
assert brand.is_displayed(), "brand filter not applied"

# Price filter  code #
price_range = driver.find_element(By.ID, "p_36/dynamic-picker-2")
price_range.click()
time.sleep(4)


#  Scroll   code #
driver.execute_script("window.scrollBy(0, 400);")
time.sleep(3)


# #  discount filter  code #
# discount = driver.find_element(By.XPATH, "//span[contains(text(),'10%')]")
# discount.click()
# time.sleep(4)

# # Assertion  RAM filter applied   #
# assert discount.is_displayed(), "discount filter not applied"

#  Pagination   code   #
pagination = driver.find_element(By.CLASS_NAME, "s-pagination-strip")
driver.execute_script("arguments[0].scrollIntoView(true);", pagination)
time.sleep(2)

next_page = driver.find_element(By.XPATH, "//a[contains(@class,'s-pagination-item')]")
next_page.click()
time.sleep(3)

# Assertion Next page opened   #
assert "page" in driver.current_url, "Pagination not working"

# Open first product   #
open_product = driver.find_element(By.CLASS_NAME, "s-image") 
open_product.click() 
time.sleep(3) 
assert open_product, "No products found"


# switch only if new tab opened
driver.switch_to.window(driver.window_handles[1])

time.sleep(4)

# Assert product detail page
product_title = driver.find_element(By.ID, "productTitle")
assert product_title.is_displayed(), "Product detail page not opened"

# Scroll
driver.execute_script("window.scrollBy(0, 400);")
time.sleep(3)

# buy now #
buy_now = driver.find_element(By.ID, "buy-now-button")
buy_now.click()

assert buy_now.is_displayed(), "buy now button  not clicked"
time.sleep(5)

driver.quit()
