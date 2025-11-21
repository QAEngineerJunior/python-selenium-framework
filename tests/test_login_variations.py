import json
from pages.login_page import LoginPage
from utils.logger import get_logger

def test_login_variations(driver,base_url):
    log = get_logger("test_login_variations")

    log.info("Starting Login Variations Test")

    creds = json.load(open("data/login_data.json"))

    for user in creds:
        log.info(f"Testing login with: {user}")

        login = LoginPage(driver)
        login.load(base_url)
        login.login(user["username"], user["password"])

        if user["username"] == "locked_out_user":
            # Expect failure
            assert "locked out" in driver.page_source.lower(), "Locked-out user did NOT show error!"
            log.info("Locked user correctly blocked.")
        else:
            # Expect success
            assert "inventory" in driver.current_url, f"User failed to log in: {user}"
            log.info("Login successful.")
