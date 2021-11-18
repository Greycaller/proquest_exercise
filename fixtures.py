import os
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture
def web_driver(request):
    """
    Web driver for general testing purposes.  Can be used normally or headless
    """
    # Set up the options
    chrome_options = Options()
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument('--start-maximized')
    if request.config.getoption("--headless"):
        chrome_options.add_argument("--headless")

    # Make the driver and return
    driver = webdriver.Chrome(executable_path=f"{os.getcwd()}/chromedriver", options=chrome_options)

    yield driver

    # Clean up after ourselves
    driver.quit()


@pytest.fixture
def headless_web_driver(request):
    """
    Headless web driver for screenshot purposes
    """
    # Set up the options
    chrome_options = Options()
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument('--start-maximized')
    chrome_options.add_argument("--headless")

    # Make the driver and return
    driver = webdriver.Chrome(executable_path=f"{os.getcwd()}/chromedriver", options=chrome_options)

    yield driver

    # Clean up after ourselves
    driver.quit()
