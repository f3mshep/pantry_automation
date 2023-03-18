from time import sleep

from selenium.webdriver.common.by import By

from browser.browser import Browser
from scraper.utils import bs

ingredient_xpath = "/html/body/div[2]/section/section[3]/section[1]/div/div/div/div[4]/div/div[3]/div[1]/div/div[4]/div/div[%s]/div[2]"

xpath = "/html/body/div[2]/section/section[3]/section[1]/div/div/div/div[4]/div/div[3]/div[1]/div/div[4]/div"

title_selection = {
    'class': 'h1',
    'attr': 'data-test-id',
    'attr_value': 'recipeDetailFragment.recipe-name'
}

ingredient_container_xpath = "/html/body/div[2]/section/section[3]/section[1]/div/div/div/div[4]/div/div[3]/div[1]/div/div[4]/div"


class HelloFreshScraper:

    def __init__(self, url):
        self.browser = Browser()
        self.url = url

    def scrape(self):
        self._vist()
        return {'title': self.get_title(), 'ingredients': self.get_ingredients()}

    def get_title(self):
        self._soup_check()
        self.hot_soup.find()
        return 't'

    def get_ingredients(self):
        results = []
        self._soup_check()
        self.hot_soup.find()
        ingredient_container = self.browser.get_element_at(ingredient_container_xpath)
        if ingredient_container is not None:
            ingredient_container_div = bs(ingredient_container)
            divs = ingredient_container_div.find_all('div')
            ps = divs[1].find_all('p')
            result = {
                'quantity':  ps[0],
                'item': ps[1]
            }
            results.append(result)
        return results

    def get_steps(self):
        return

    def _soup_check(self):
        if self.hot_soup is None:
            raise Exception("NO SOUP FOR YOU!")

    def _vist(self):
        self.browser.visit(self.url)
        html = self.browser.show_source(wait_element=ingredient_container_xpath, by=By.XPATH)
        if html is not None:
            self.hot_soup = bs(html)
