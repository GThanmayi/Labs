from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import time

driver = webdriver.Chrome()
driver.get("https://tutorialsninja.com/demo/")

print("Page loaded — implicit wait enabled.")

# Implicit wait
driver.implicitly_wait(10)

try:
    # Explicit wait: wait until search box is clickable
    wait = WebDriverWait(driver, 15)
    search_box = wait.until(
        EC.element_to_be_clickable((By.NAME, "search"))
    )
    print("Search box is clickable ")
    search_box.send_keys("MacBook")

    search_button = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button.btn-default.btn-lg"))
    )
    search_button.click()
    print("Clicked Search button ")

except Exception as e:
    print("Explicit wait failed:", e)

# Fluent wait: wait for first product image to appear
fluent_wait = WebDriverWait(driver, 20, poll_frequency=2, ignored_exceptions=[NoSuchElementException])
try:
    first_product = fluent_wait.until(
        EC.element_to_be_clickable((By.XPATH, "//div[@class='product-thumb']//img"))
    )
    print("Fluent wait success — product visible!")
    print("Ready to interact with product.")
    first_product.click()
except Exception as e:
    print("Fluent wait timed out:", e)

time.sleep(2)
driver.quit()
