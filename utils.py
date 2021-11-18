from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from constants import (google_url,
                       google_search_selector)


def google_proquest(web_driver):
    # Search for ProQuest
    web_driver.get(url=google_url)
    web_driver.find_element_by_css_selector(css_selector=google_search_selector).send_keys("ProQuest")
    web_driver.find_element_by_css_selector(css_selector=google_search_selector).send_keys(Keys.RETURN)

    # Wait for the page to load
    WebDriverWait(web_driver, 3).until(EC.visibility_of_element_located((By.ID, "result-stats")))


def save_screenshot(headless_web_driver, file_name):
    # Adjust the window size so we get everything in one screenshot
    original_size = headless_web_driver.get_window_size()
    required_width = headless_web_driver.execute_script('return document.body.parentNode.scrollWidth')
    required_height = headless_web_driver.execute_script('return document.body.parentNode.scrollHeight')
    headless_web_driver.set_window_size(required_width, required_height)

    # Take the screenshot
    headless_web_driver.find_element_by_tag_name("body").screenshot(file_name)

    # Clean up after ourselves
    headless_web_driver.set_window_size(original_size['width'], original_size['height'])
