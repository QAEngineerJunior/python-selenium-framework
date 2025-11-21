from pages.login_page import LoginPage
from utils.logger import get_logger

def test_invalid_login(driver,base_url):
    log = get_logger("test_invalid_login")

    log.info("Starting Invalid Login Test")

    login = LoginPage(driver)
    log.info("Loading login page...")
    login.load(base_url)

    log.info("Attempting login with WRONG credentials...")
    login.login("wrong_user", "wrong_pass")

    log.info("Checking for error message...")
    assert "Epic sadface" in driver.page_source, "Error message NOT displayed!"

    log.info("TEST PASS: Invalid login shows correct error message.")
