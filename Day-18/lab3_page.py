from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

class Lab3Page:

    def __init__(self, driver):
        self.driver = driver

    # Locators
    demo_link = (By.LINK_TEXT, "https://tutorialsninja.com/demo")
    desktops_menu = (By.LINK_TEXT, "Desktops")
    mac_option = (By.LINK_TEXT, "Mac (1)")
    sort_dropdown = (By.ID, "input-sort")
    product_link = (By.CSS_SELECTOR, "p:nth-child(2)")
    add_to_cart_button = (By.CSS_SELECTOR, ".button-group .hidden-xs")

    # Actions
    def open_demo_site(self):
        self.driver.find_element(*self.demo_link).click()

    def click_desktops(self):
        self.driver.find_element(*self.desktops_menu).click()

    def click_mac(self):
        self.driver.find_element(*self.mac_option).click()

    def sort_by_name_az(self):
        dropdown = Select(self.driver.find_element(*self.sort_dropdown))
        dropdown.select_by_visible_text("Name (A - Z)")

    def open_product(self):
        self.driver.find_element(*self.product_link).click()

    def add_to_cart(self):
        self.driver.find_element(*self.add_to_cart_button).click()
