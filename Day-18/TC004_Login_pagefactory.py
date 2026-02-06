#from Day18 import Loginpage_pageFactory
from Day18.Loginpage_PageFactory import loginpage_PageFactory
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
import time

driver = webdriver.Firefox()
driver.implicitly_wait(10)
wait = WebDriverWait(driver, 10)

driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
time.sleep(2)
loginobj = loginpage_PageFactory(driver)
loginobj.enterusername("Admin")
loginobj.enterpassword("admin123")
loginobj.clicklogin()
