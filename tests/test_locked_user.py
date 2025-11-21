from pages.login_page import LoginPage
from utils.logger import get_logger

def test_locked_user(driver,base_url):
    log = get_logger("test_locked_user")

    log.info("Starting Locked User Test")

    login = LoginPage(driver)
    log.info("Loading login page...")
    login.load(base_url)

    log.info("Logging in with locked_out_user...")
    login.login("locked_out_user", "secret_sauce")

    log.info("Validating locked-out message...")
    assert "locked out" in driver.page_source.lower(), "Locked out message NOT shown!"

    log.info("TEST PASS: Locked user message displayed correctly.")


