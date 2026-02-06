from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from Day18.Loginpage import Loginpage

driver = webdriver.Firefox()
driver.implicitly_wait(10)
wait = WebDriverWait(driver, 10)

driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

loginobj = Loginpage(driver)
loginobj.enterusername("Admin")
loginobj.enterpassword("admin123")
loginobj.clicklogin()
