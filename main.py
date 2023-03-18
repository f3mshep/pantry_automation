from scraper.hello_fresh_scraper import HelloFreshScraper

if __name__ == '__main__':
    scraper = HelloFreshScraper("https://www.hellofresh.com/recipes/cherry-mozz-grilled-cheese-with-pickled-shallot-6407797f5903f7c86905fce9")
    print(scraper.scrape())