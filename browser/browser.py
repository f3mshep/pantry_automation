from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from undetected_chromedriver import ChromeOptions
import undetected_chromedriver as uc


def _get_options():
    options = ChromeOptions()
    options.add_argument('--headless')
    return options


class Browser:
    driver = None

    def __init__(self):
        self.driver = uc.Chrome(options=_get_options())

    def visit(self, url):
        self.driver.get(url)

    def show_source(self, **kwargs):
        wait_element = kwargs.pop('wait_element')
        by = kwargs.pop('by')
        if wait_element is not None and by is not None:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(
                (by, wait_element)))

        return self.driver.execute_script("return document.documentElement.outerHTML")

    def get_element_at(self, xpath):
        self.driver.find_element(By.XPATH, xpath)

    def quit(self):
        self.driver.quit()
