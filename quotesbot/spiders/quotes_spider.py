import scrapy
from scrapy_splash import SplashRequest

from quotesbot.items import QuoteItem


class QuotesSpider(scrapy.Spider):
    name = "quotes"

    def start_requests(self):  # pragma: no cover
        url = "https://quotes.toscrape.com/js/"
        yield SplashRequest(url=url, callback=self.parse)

    def parse(self, response):
        for quote in response.css("div.quote"):
            quote_item = QuoteItem(
                quote=quote.css("span.text::text").get(),
                author=quote.css("small.author::text").get(),
                tags=quote.css("div.tags a.tag::text").getall(),
            )
            yield quote_item

        next_page = response.css("li.next a::attr(href)").get()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield SplashRequest(next_page, callback=self.parse)
