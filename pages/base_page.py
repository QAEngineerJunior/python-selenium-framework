from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from utils.logger import get_logger

class BasePage:
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.timeout = timeout
        self.wait = WebDriverWait(driver, timeout)
        self.log = get_logger(self.__class__.__name__)

    # -----------------------------
    # BASIC ELEMENT INTERACTIONS
    # -----------------------------
    def click(self, locator):
        self.log.info(f"Clicking on element: {locator}")
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()

    def type(self, locator, text):
        self.log.info(f"Typing '{text}' into: {locator}")
        element = self.wait.until(EC.visibility_of_element_located(locator))
        element.clear()
        element.send_keys(text)

    def get_text(self, locator):
        self.log.info(f"Getting text from: {locator}")
        element = self.wait.until(EC.visibility_of_element_located(locator))
        return element.text

    # -----------------------------
    # ADVANCED WAITS
    # -----------------------------
    def wait_visible(self, locator):
        self.log.info(f"Waiting for visibility: {locator}")
        return self.wait.until(EC.visibility_of_element_located(locator))

    def wait_clickable(self, locator):
        self.log.info(f"Waiting for clickable: {locator}")
        return self.wait.until(EC.element_to_be_clickable(locator))

    def wait_text(self, locator, text):
        self.log.info(f"Waiting for text '{text}' in {locator}")
        return self.wait.until(EC.text_to_be_present_in_element(locator, text))

    def wait_url_contains(self, value):
        self.log.info(f"Waiting for URL to contain: {value}")
        return self.wait.until(EC.url_contains(value))

    # -----------------------------
    # SAFE CHECKS
    # -----------------------------
    def exists(self, locator):
        self.log.info(f"Checking existence of: {locator}")
        try:
            self.driver.find_element(*locator)
            return True
        except NoSuchElementException:
            return False

    # -----------------------------
    # ADVANCED ACTIONS
    # -----------------------------
    def scroll_to(self, locator):
        self.log.info(f"Scrolling to: {locator}")
        element = self.wait_visible(locator)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)

    def js_click(self, locator):
        self.log.info(f"JS clicking: {locator}")
        element = self.wait_clickable(locator)
        self.driver.execute_script("arguments[0].click();", element)

    def hover(self, locator):
        self.log.info(f"Hovering over: {locator}")
        element = self.wait_visible(locator)
        ActionChains(self.driver).move_to_element(element).perform()
