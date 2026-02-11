import pytest
from driverfactory import get_driver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.mark.parametrize("browser", ["chrome", "edge"])
def test_googletitle(browser):
    driver = get_driver(browser)
    driver.get("https://www.google.com")

    # WAIT until the title contains "Google"
    WebDriverWait(driver, 10).until(EC.title_contains("Google"))

    assert "Google" in driver.title  # ✔ correct
    driver.quit()

@pytest.mark.parametrize("browser", ["chrome", "edge"])
def test_google_search(browser):
    driver = get_driver(browser)
    driver.get("https://www.google.com")

    # wait search box to appear
    search_box = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "q"))
    )

    search_box.send_keys("selenium grid")
    search_box.submit()

    # wait for results page — title should change
    WebDriverWait(driver, 10).until(EC.title_contains("selenium grid"))

    assert "selenium grid" in driver.title.lower()  # ✔ correct
    driver.quit()
