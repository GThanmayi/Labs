from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Chrome()
driver.get("https://tutorialsninja.com/demo")
driver.maximize_window()

# Go to Register page
driver.find_element(By.LINK_TEXT, "My Account").click()
driver.find_element(By.LINK_TEXT, "Register").click()

# 1️⃣ Fill text boxes
driver.find_element(By.ID, "input-firstname").send_keys("Thanmayi")
driver.find_element(By.ID, "input-lastname").send_keys("G")
driver.find_element(By.ID, "input-email").send_keys("thanmayi123@gmail.com")
driver.find_element(By.ID, "input-telephone").send_keys("9876543210")
driver.find_element(By.ID, "input-password").send_keys("Test@123")
driver.find_element(By.ID, "input-confirm").send_keys("Test@123")

# 2️⃣ Select radio button
driver.find_element(By.NAME, "newsletter").click()

# 3️⃣ Select checkbox
driver.find_element(By.NAME, "agree").click()

# 4️⃣ Submit the form
driver.find_element(By.XPATH, "//input[@value='Continue']").click()

# Verify confirmation message
confirmation = driver.find_element(By.TAG_NAME, "h1").text
print("Confirmation message:", confirmation)

driver.quit()
