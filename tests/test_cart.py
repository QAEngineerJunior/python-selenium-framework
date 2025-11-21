from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from utils.logger import get_logger

def test_cart_items(driver,base_url):
    log = get_logger("test_cart")

    log.info("Starting Cart Test")

    log.info("Loading login page...")
    login = LoginPage(driver)
    login.load(base_url)


    log.info("Logging in with correct credentials...")
    login.login("standard_user", "secret_sauce")

    log.info("Adding items to cart...")
    products = ProductsPage(driver)
    products.add_items()

    log.info("Navigating to cart...")
    products.go_to_cart()

    log.info("Retrieving items from the cart...")
    items = products.get_cart_items()
    log.info(f"Items found in cart: {items}")

    log.info("Validating items...")
    assert "Sauce Labs Backpack" in items, "Backpack missing"
    assert "Sauce Labs Bike Light" in items, "Bike Light missing"

    log.info("TEST PASS: Cart contains correct items.")

