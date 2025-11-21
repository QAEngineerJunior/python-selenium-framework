from selenium import webdriver

# OPTIONS
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.options import Options as EdgeOptions

# SERVICES
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService

# DRIVER MANAGERS
from webdriver_manager.chrome import ChromeDriverManager


def create_driver(browser_name="chrome"):
    browser_name = browser_name.lower()

    # ============ CHROME =============
    if browser_name == "chrome":
        options = ChromeOptions()
        options.add_experimental_option("prefs", {
            "credentials_enable_service": False,
            "profile.password_manager_enabled": False,
            "profile.password_manager_leak_detection": False
        })
        options.add_argument("--disable-features=PasswordManagerEnabled,PasswordCheck,PasswordLeakDetection,AutoSubmitPasswordChanges")

        service = ChromeService(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=options)

    # ============ FIREFOX ============
    elif browser_name == "firefox":
        options = FirefoxOptions()
        options.set_preference("dom.webnotifications.enabled", False)

        driver = webdriver.Firefox(options=options)  # Local geckodriver

    # ============= EDGE ==============
    elif browser_name == "edge":
        options = EdgeOptions()

        service = EdgeService()  # Local msedgedriver (from PATH)
        driver = webdriver.Edge(service=service, options=options)

    else:
        raise ValueError(f"Unsupported browser: {browser_name}")

    driver.maximize_window()
    return driver


