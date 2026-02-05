from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Chrome()
driver.get("https://www.techlistic.com/p/selenium-practice-form.html")
driver.maximize_window()
time.sleep(2)

# Fill text boxes
driver.find_element(By.NAME, "firstname").send_keys("Thanmayi")
driver.find_element(By.NAME, "lastname").send_keys("G")

# Scroll to gender radio button
gender_radio = driver.find_element(By.ID, "sex-0")
driver.execute_script("arguments[0].scrollIntoView(true);", gender_radio)
time.sleep(1)

# Click radio using JavaScript (avoids ad issue)
driver.execute_script("arguments[0].click();", gender_radio)

# Experience radio
exp_radio = driver.find_element(By.ID, "exp-4")
driver.execute_script("arguments[0].click();", exp_radio)

# Date
driver.find_element(By.ID, "datepicker").send_keys("10-10-2025")

# Checkboxes
profession = driver.find_element(By.ID, "profession-1")
driver.execute_script("arguments[0].click();", profession)

tool = driver.find_element(By.ID, "tool-2")
driver.execute_script("arguments[0].click();", tool)

# Dropdown using Select
continent = Select(driver.find_element(By.ID, "continents"))
continent.select_by_visible_text("Europe")

# Scroll and submit
submit_btn = driver.find_element(By.ID, "submit")
driver.execute_script("arguments[0].scrollIntoView(true);", submit_btn)
driver.execute_script("arguments[0].click();", submit_btn)

print("✅ Form filled and submitted successfully")

time.sleep(3)
driver.quit()
