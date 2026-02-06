from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

class Lab3Page_pagefactory:

    def __init__(self, driver):
        self.driver = driver

    # Page Factory style elements
    @property
    def demo_link(self):
        return self.driver.find_element(By.LINK_TEXT, "https://tutorialsninja.com/demo")

    @property
    def desktops_menu(self):
        return self.driver.find_element(By.LINK_TEXT, "Desktops")

    @property
    def mac_option(self):
        return self.driver.find_element(By.LINK_TEXT, "Mac (1)")

    @property
    def sort_dropdown(self):
        return self.driver.find_element(By.ID, "input-sort")

    @property
    def product_link(self):
        return self.driver.find_element(By.CSS_SELECTOR, "p:nth-child(2)")

    @property
    def add_to_cart_button(self):
        return self.driver.find_element(By.CSS_SELECTOR, ".button-group .hidden-xs")

    # Actions
    def open_demo_site(self):
        self.demo_link.click()

    def click_desktops(self):
        self.desktops_menu.click()

    def click_mac(self):
        self.mac_option.click()

    def sort_by_name_az(self):
        Select(self.sort_dropdown).select_by_visible_text("Name (A - Z)")

    def open_product(self):
        self.product_link.click()

    def add_to_cart(self):
        self.add_to_cart_button.click()
