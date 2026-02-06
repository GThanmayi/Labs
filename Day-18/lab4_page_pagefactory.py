from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

class Lab4PageFactory:

    def __init__(self, driver):
        self.driver = driver

    # -------- Page Factory Elements --------
    @property
    def demo_link(self):
        return self.driver.find_element(By.LINK_TEXT, "https://tutorialsninja.com/demo")

    @property
    def desktops_link(self):
        return self.driver.find_element(By.LINK_TEXT, "Desktops")

    @property
    def mac_link(self):
        return self.driver.find_element(By.LINK_TEXT, "Mac (1)")

    @property
    def headers(self):
        return self.driver.find_elements(By.CSS_SELECTOR, "h2")

    @property
    def sort_dropdown(self):
        return self.driver.find_element(By.ID, "input-sort")

    @property
    def add_to_cart_button(self):
        return self.driver.find_element(By.CSS_SELECTOR, ".button-group .hidden-xs")

    @property
    def search_box(self):
        return self.driver.find_element(By.NAME, "search")

    @property
    def search_button(self):
        return self.driver.find_element(By.CSS_SELECTOR, ".input-group-btn > .btn")

    @property
    def description_checkbox(self):
        return self.driver.find_element(By.ID, "description")

    @property
    def search_page_button(self):
        return self.driver.find_element(By.ID, "button-search")

    # -------- Actions --------
    def open_demo_site(self):
        self.demo_link.click()

    def open_desktops(self):
        self.desktops_link.click()

    def open_mac(self):
        self.mac_link.click()

    def verify_headers_present(self):
        return len(self.headers) > 0

    def sort_by_name_az(self):
        Select(self.sort_dropdown).select_by_visible_text("Name (A - Z)")

    def add_to_cart(self):
        self.add_to_cart_button.click()

    def search_product(self, product):
        self.search_box.clear()
        self.search_box.send_keys(product)
        self.search_button.click()

    # FIXED METHOD (this was crashing before)
    def advanced_search(self, product):
        self.search_box.clear()
        self.search_box.send_keys(product)
        self.description_checkbox.click()
        self.search_page_button.click()
