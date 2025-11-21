from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

options = Options()

options.add_experimental_option("prefs", {
    "credentials_enable_service": False,
    "profile.password_manager_enabled": False,
    "profile.password_manager_leak_detection": False
})

options.add_argument("--disable-features=PasswordManagerEnabled,PasswordCheck,PasswordLeakDetection,AutoSubmitPasswordChanges")
options.add_argument("--disable-save-password-bubble")

driver = webdriver.Chrome(options=options)


driver.get("http://www.saucedemo.com")
# username 
username_box = driver.find_element(By.ID, "user-name")
username_box.send_keys("standard_user")
# password
password_box = driver.find_element(By.ID, "password")
password_box.send_keys("secret_sauce")
# login
login_button = driver.find_element(By.ID, "login-button")
login_button.click()
# Add first item to cart
item1 = driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack")
item1.click()

# Add second item to cart
item2 = driver.find_element(By.ID, "add-to-cart-sauce-labs-bike-light")
item2.click()

# Go to cart
cart_button = driver.find_element(By.CLASS_NAME, "shopping_cart_link")
cart_button.click()

# Verify that both items are present in the cart
cart_items = driver.find_elements(By.CLASS_NAME, "inventory_item_name")

item_names = [item.text for item in cart_items]

if "Sauce Labs Backpack" in item_names and "Sauce Labs Bike Light" in item_names:
    print("TEST PASS: Both items are in the cart.")
else:
    print("TEST FAIL: Missing items in the cart.")




# handle cookie consent popup if it appears
try:
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "L2AGLb"))
    ).click()
except:
    print("No cookie popup appeared")

# search 
search_box = driver.find_element(By.NAME, "q")
search_box.send_keys("Python automation with Selenium")
search_box.send_keys(Keys.ENTER)

time.sleep(5)

driver.quit()
