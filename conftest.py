def pytest_addoption(parser):
    parser.addoption('--headless', help="Run webdriver in headless mode", action="store_true")
