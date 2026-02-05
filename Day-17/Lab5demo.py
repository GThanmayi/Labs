from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Launch Firefox
driver = webdriver.Firefox()
wait = WebDriverWait(driver, 15)

# Open URL
driver.get("https://tutorialsninja.com/demo")
driver.maximize_window()

# Verify title
print("Page Title:", driver.title)
assert "Your Store" in driver.title
print("✅ Title verified")

# My Account → Register
wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "My Account"))).click()
wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Register"))).click()

# Verify Register page using URL
print("Current URL:", driver.current_url)
assert "route=account/register" in driver.current_url
print("✅ Register page verified using URL")

# Click Continue without filling form
wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@value='Continue']"))).click()

# Verify Privacy Policy warning
warning = wait.until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, ".alert-danger"))
).text

assert "Privacy Policy" in warning
print("✅ Privacy policy warning verified")

# -------- Fill ONLY available fields --------
driver.find_element(By.ID, "input-firstname").send_keys("Thanmayi")
driver.find_element(By.ID, "input-lastname").send_keys("G")
driver.find_element(By.ID, "input-email").send_keys("thanmayi" + str(int(time.time())) + "@gmail.com")
driver.find_element(By.ID, "input-telephone").send_keys("9876543210")

driver.find_element(By.ID, "input-password").send_keys("test1234")
driver.find_element(By.ID, "input-confirm").send_keys("test1234")

# Newsletter → Yes
driver.find_element(By.XPATH, "//input[@name='newsletter' and @value='1']").click()

# Accept Privacy Policy
driver.find_element(By.NAME, "agree").click()

# Click Continue
driver.find_element(By.XPATH, "//input[@value='Continue']").click()

# -------- SUCCESS VERIFICATION (FIXED) --------
assert "route=account/success" in driver.current_url
print("✅ Account created successfully (verified by URL)")

# Click Continue on success page
wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Continue"))).click()

print("🎉 Test executed successfully")

time.sleep(3)
driver.quit()
