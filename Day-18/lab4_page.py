from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

class Lab4Page:

    def __init__(self, driver):
        self.driver = driver

    # Locators
    demo_link = (By.LINK_TEXT, "https://tutorialsninja.com/demo")
    desktops_link = (By.LINK_TEXT, "Desktops")
    mac_link = (By.LINK_TEXT, "Mac (1)")
    sort_dropdown = (By.ID, "input-sort")
    add_to_cart_btn = (By.CSS_SELECTOR, ".button-group .hidden-xs")
    search_box = (By.NAME, "search")
    search_button = (By.CSS_SELECTOR, ".input-group-btn > .btn")
    description_checkbox = (By.ID, "description")
    search_page_btn = (By.ID, "button-search")
    headers = (By.CSS_SELECTOR, "h2")

    # Actions
    def open_demo_site(self):
        self.driver.find_element(*self.demo_link).click()

    def open_desktops(self):
        self.driver.find_element(*self.desktops_link).click()

    def open_mac(self):
        self.driver.find_element(*self.mac_link).click()

    def verify_headers_present(self):
        elements = self.driver.find_elements(*self.headers)
        return len(elements) > 0

    def sort_by_name_az(self):
        dropdown = Select(self.driver.find_element(*self.sort_dropdown))
        dropdown.select_by_visible_text("Name (A - Z)")

    def add_to_cart(self):
        self.driver.find_element(*self.add_to_cart_btn).click()

    def search_product(self, product_name):
        self.driver.find_element(*self.search_box).send_keys(product_name)
        self.driver.find_element(*self.search_button).click()

    def advanced_search(self, product_name):
        self.driver.find_element(*self.search_box).clear()
        self.driver.find_element(*self.search_box).send_keys(product_name)
        self.driver.find_element(*self.description_checkbox).click()
        self.driver.find_element(*self.search_page_btn).click()
