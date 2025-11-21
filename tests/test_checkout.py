from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from pages.checkout_page import CheckoutPage
from utils.logger import get_logger

def test_full_checkout(driver,base_url):
    log = get_logger("test_checkout")

    log.info("Starting Full Checkout Test")

    login = LoginPage(driver)
    log.info("Loading login page...")
    login.load(base_url)

    log.info("Logging in as standard_user...")
    login.login("standard_user", "secret_sauce")

    log.info("Adding items to cart...")
    products = ProductsPage(driver)
    products.add_items()

    log.info("Navigating to cart...")
    products.go_to_cart()

    log.info("Starting checkout process...")
    checkout = CheckoutPage(driver)
    checkout.start_checkout()

    log.info("Filling out customer information...")
    checkout.fill_information("Miguel", "Van Mechgelen", "1234")

    log.info("Finishing checkout...")
    checkout.finish_checkout()

    confirmation = checkout.get_confirmation()
    log.info(f"Confirmation message: {confirmation}")

    assert "THANK YOU" in confirmation.upper(), "Checkout did NOT complete!"

    log.info("TEST PASS: Full checkout flow completed successfully.")
