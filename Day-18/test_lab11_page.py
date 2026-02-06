import pytest
from selenium import webdriver
from Day18.lab4_page import Lab4Page

class TestLab4POM:

    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def teardown_method(self):
        self.driver.quit()

    def test_lab4(self):
        self.driver.get("https://tutorialsninja.com/")

        page = Lab4Page(self.driver)

        page.open_demo_site()
        page.open_desktops()
        page.open_mac()

        assert page.verify_headers_present()

        page.sort_by_name_az()
        page.add_to_cart()

        self.driver.execute_script("window.scrollTo(0,324)")

        page.search_product("Monitors")
        page.advanced_search("Monitors")
