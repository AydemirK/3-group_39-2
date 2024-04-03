import httpx
import asyncio
from parsel import Selector


class AsyncScraper:
    URL = 'http://www.tazabek.kg/reviews/page:{page}'
    HEADERS = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
        "Accept-Language": "ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:124.0) Gecko/20100101 Firefox/124.0"
    }
    ADVERTISING_URL = '//div[@class="card-view weight-title"]/a/@href'

    async def fetch_page(self, client, page):
        url = self.URL.format(page=page)
        response = await client.get(url, timeout=15.0)
        print(response.url)
        if response.status_code == 200:
            return Selector(text=response.text)
        else:
            print(f'Erorr page {page}')
            response.raise_for_status()

    async def scrape_page(self, selector):
        links = selector.xpath(self.ADVERTISING_URL).getall()
        print(links)

    async def get_pages(self, limit=5):
        async with httpx.AsyncClient(headers=self.HEADERS) as session:
            tasks = [self.fetch_page(session, page) for page in range(1, limit + 1)]
            pages = await asyncio.gather(*tasks)
            scraper_tasks = [self.scrape_page(selector=selector) for selector in pages if pages is not None]
            await asyncio.gather(*scraper_tasks)

    # def scrape(self):
    #     page = requests.request("GET", url=self.URL, headers=self.HEADERS)
    #     tree = Selector(text=page.text)
    #     link_Commerce_Advertising = tree.xpath(self.ADVERTISING_URL).getall()
    #
    #     return link_Commerce_Advertising[:5]


if __name__ == '__main__':
    scraper = AsyncScraper()
    asyncio.run(scraper.get_pages())
