import pytest
import pytest_html
from utils.browser import create_driver
from utils.screenshots import take_screenshot

@pytest.fixture()
def base_url(request):
    from config.settings import load_environment
    env = request.config.getoption("--env")
    return load_environment(env)

@pytest.fixture()
def driver(request, browser_name):
    driver = create_driver(browser_name)
    yield driver

    if request.node.rep_call.failed:
        screenshot_path = take_screenshot(driver, request.node.name)
        print(f"Screenshot saved: {screenshot_path}")

    driver.quit()



# --- Pytest Hook: enables rep_call (test result object) ---
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="Browser: chrome, firefox, edge")
    parser.addoption("--env", action="store", default="dev", help="Environment to run tests against")
@pytest.fixture()
def browser_name(request):
    return request.config.getoption("--browser")


