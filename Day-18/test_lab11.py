from selenium import webdriver
from Day18.lab3_page import Lab3Page
print("TEST FILE LOADED")

class TestLab3:

    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def teardown_method(self):
        self.driver.quit()

    def test_lab3(self):
        self.driver.get("https://tutorialsninja.com/")

        page = Lab3Page(self.driver)

        page.open_demo_site()
        page.click_desktops()
        page.click_mac()
        page.sort_by_name_az()
        page.open_product()
        page.add_to_cart()

        self.driver.execute_script("window.scrollTo(0,324)")
