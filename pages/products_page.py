from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class ProductsPage(BasePage):

    BACKPACK = (By.ID, "add-to-cart-sauce-labs-backpack")
    BIKE_LIGHT = (By.ID, "add-to-cart-sauce-labs-bike-light")
    CART_BTN = (By.CLASS_NAME, "shopping_cart_link")
    ITEM_NAMES = (By.CLASS_NAME, "inventory_item_name")

    def __init__(self, driver):
        self.driver = driver
        super().__init__(driver)        

    def add_items(self):
        self.click(self.BACKPACK)
        self.click(self.BIKE_LIGHT)

    def go_to_cart(self):
        self.click(self.CART_BTN)

    def get_cart_items(self):
        elements = self.driver.find_elements(*self.ITEM_NAMES)
        return [el.text for el in elements]
    
