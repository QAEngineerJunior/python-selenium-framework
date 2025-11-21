import os
from datetime import datetime

def take_screenshot(driver, name="failure"):
    # Create folder if missing
    if not os.path.exists("screenshots"):
        os.makedirs("screenshots")

    # Create filename
    filename = f"screenshots/{name}_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.png"

    # Save screenshot
    driver.save_screenshot(filename)
    return filename

