from selenium import webdriver
from selenium.webdriver.common.by import By

import time

driver=webdriver.Firefox()
driver.get("https://tutorialsninja.com/")
driver.maximize_window()
print("title is",driver.title)
driver.get("https://www.google.com")
print("title is",driver.title)
time.sleep(5)
driver.back()
print("title after back is",driver.title)
driver.forward()
print("title after forward is",driver.title)
driver.quit()  #to close the browser