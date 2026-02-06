from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium import webdriver

class Lab4Page:

    def __init__(self, driver):
        self.driver = driver

    # Locators
    demo_link = (By.LINK_TEXT, "https://tutorialsninja.com/demo")
    desktops = (By.LINK_TEXT, "Desktops")
    mac = (By.LINK_TEXT, "Mac (1)")
    sort_dropdown = (By.ID, "input-sort")
    add_to_cart = (By.CSS_SELECTOR, ".button-group .hidden-xs")
    headers = (By.CSS_SELECTOR, "h2")
    search_box = (By.NAME, "search")
    search_btn = (By.CSS_SELECTOR, ".input-group-btn > .btn")
    description = (By.ID, "description")
    search_page_btn = (By.ID, "button-search")

    # Reusable actions
    def click(self, locator):
        self.driver.find_element(*locator).click()

    def type(self, locator, text):
        el = self.driver.find_element(*locator)
        el.clear()
        el.send_keys(text)

    def select_by_text(self, locator, value):
        Select(self.driver.find_element(*locator)).select_by_visible_text(value)

    # Page flows (Lab4)
    def open_demo(self):
        self.click(self.demo_link)

    def open_mac_desktops(self):
        self.click(self.desktops)
        self.click(self.mac)

    def verify_headers(self):
        return len(self.driver.find_elements(*self.headers)) > 0

    def sort_products(self):
        self.select_by_text(self.sort_dropdown, "Name (A - Z)")

    def add_product_to_cart(self):
        self.click(self.add_to_cart)

    def search_product(self, name):
        self.type(self.search_box, name)
        self.click(self.search_btn)

    def advanced_search(self, name):
        self.type(self.search_box, name)
        self.click(self.description)
        self.click(self.search_page_btn)



class TestLab4:

    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://tutorialsninja.com/")

    def teardown_method(self):
        self.driver.quit()

    def test_lab4(self):
        page = Lab4Page(self.driver)

        page.open_demo()
        page.open_mac_desktops()

        assert page.verify_headers()

        page.sort_products()
        page.add_product_to_cart()

        self.driver.execute_script("window.scrollTo(0,300)")

        page.search_product("Monitors")
        page.advanced_search("Monitors")



class TestLab4:

    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://tutorialsninja.com/")

    def teardown_method(self):
        self.driver.quit()

    def test_lab4(self):
        page = Lab4Page(self.driver)

        page.open_demo()
        page.open_mac_desktops()

        assert page.verify_headers()

        page.sort_products()
        page.add_product_to_cart()

        self.driver.execute_script("window.scrollTo(0,300)")

        page.search_product("Monitors")
        page.advanced_search("Monitors")
