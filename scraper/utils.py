from bs4 import BeautifulSoup


def bs(content):
    return BeautifulSoup(content, 'html.parser')