import requests
from parsel import Selector


class NewsScraper:

    URL = 'https://diesel.elcat.kg/'
    HEADERS = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
        "Accept-Language": "ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:124.0) Gecko/20100101 Firefox/124.0"
    }
    ADVERTISING_URL = '//td[@class="col_c_forum"]/h4/a/@href'
    ADVERTISING_TITLE = '//td[@class="col_c_forum"]/h4/a[@title]/text()'

    def scrape(self):
        page = requests.request("GET", url=self.URL, headers=self.HEADERS)
        tree = Selector(text=page.text)
        link_Commerce_Advertising = tree.xpath(self.ADVERTISING_URL).getall()

        return link_Commerce_Advertising[:5]
