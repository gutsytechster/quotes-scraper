import scrapy
from scrapy_splash import SplashRequest


class QuotesSpider(scrapy.Spider):
    name = "quotes"

    def start_requests(self):
        url = "https://quotes.toscrape.com/js/"
        yield SplashRequest(
            url=url, callback=self.parse
        )

    def parse(self, response):
        for quote in response.css("div.quote"):
            yield {
                "quote": quote.css('span.text::text').get(),
                "author": quote.css('small.author::text').get(),
                "tags": quote.css('div.tags a.tag::text').getall(),
            }
        next_page = response.css('li.next a::attr(href)').get()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield SplashRequest(next_page, callback=self.parse)
