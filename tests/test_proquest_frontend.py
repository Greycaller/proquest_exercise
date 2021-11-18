from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from constants import (google_search_bar_id,
                       google_title_selector,
                       google_result_txt,
                       proquest_link_text,
                       proquest_search_bar_name,
                       proquest_results_header_class,
                       qa_search_screenshot)
from fixtures import (web_driver,
                      headless_web_driver)
from utils import (google_proquest,
                   save_screenshot)


def test_google_search(web_driver):
    # Google ProQuest
    google_proquest(web_driver=web_driver)

    # Grab the titles of all results on the first page and make sure we're only grabbing results in the search area
    search_element = web_driver.find_element_by_id(id_=google_search_bar_id)
    # Search using this selector because not all titles share the same class name(s)
    title_elements = search_element.find_elements_by_css_selector(css_selector=google_title_selector)

    # Get the human-readable text
    search_titles = []
    for element in title_elements:
        # 'People Also Ask' comes back as an empty string so use this chance to weed those out
        if element.text is not '':
            search_titles.append(element.text)

    # Write results to file
    with open(google_result_txt, 'w') as output:
        output.write(str(search_titles))
        output.close()


def test_qa_page_screenshot(headless_web_driver):
    # Google ProQuest
    google_proquest(web_driver=headless_web_driver)

    # From the results navigate to the ProQuest website and wait for the page to load
    headless_web_driver.find_element_by_partial_link_text(link_text=proquest_link_text).click()
    WebDriverWait(headless_web_driver, 3).until(EC.visibility_of_element_located((By.NAME, proquest_search_bar_name)))

    # Search for 'QA' and wait for the page to load
    headless_web_driver.find_element_by_name(name=proquest_search_bar_name).send_keys("QA")
    headless_web_driver.find_element_by_name(name=proquest_search_bar_name).send_keys(Keys.RETURN)
    WebDriverWait(headless_web_driver, 3).until(EC.visibility_of_element_located((By.CLASS_NAME,
                                                                                  proquest_results_header_class)))

    # Take our screenshot
    save_screenshot(headless_web_driver=headless_web_driver, file_name=qa_search_screenshot)
