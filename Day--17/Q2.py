from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://letcode.in/alert")
driver.maximize_window()

# 1️⃣ Trigger simple alert
driver.find_element(By.ID, "accept").click()
alert = driver.switch_to.alert

# 2️⃣ Accept alert and print message
print("Alert message:", alert.text)
alert.accept()
time.sleep(1)

# 3️⃣ Dismiss confirmation pop-up
driver.find_element(By.ID, "confirm").click()
alert = driver.switch_to.alert
print("Confirm alert message:", alert.text)
alert.dismiss()
time.sleep(5)

# 4️⃣ Enter text in prompt alert and accept
driver.find_element(By.ID, "prompt").click()
alert = driver.switch_to.alert
alert.send_keys("Thanmayi")
alert.accept()
time.sleep(5)

# 5️⃣ Verify result displayed on page
result_text = driver.find_element(By.ID, "myName").text
print("Result displayed on page:", result_text)

driver.quit()
