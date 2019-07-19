# -*- coding: utf-8 -*-
import scrapy
from scrapy.loader import ItemLoader
from scrap_goodreads_qoutes.items import QuoteItem

class GoodreadesSpider(scrapy.Spider):
    # identity
    name = 'goodreads'

    # request
    def start_requests(self):
        # urls = [
        #     'https://www.goodreads.com/quotes?page=1',
        #     'https://www.goodreads.com/quotes?page=2',
        #     'https://www.goodreads.com/quotes?page=3',
        #     'https://www.goodreads.com/quotes?page=4',
        #     'https://www.goodreads.com/quotes?page=5',
        #     'https://www.goodreads.com/quotes?page=6',
        #     'https://www.goodreads.com/quotes?page=7',
        #     'https://www.goodreads.com/quotes?page=8',
        #     'https://www.goodreads.com/quotes?page=9',
        #     'https://www.goodreads.com/quotes?page=10',
        # ]
        # for url in urls:
        #     yield scrapy.Request(url=url, callback=self.parse)

        url = 'https://www.goodreads.com/quotes?page=1'
        yield scrapy.Request(url=url, callback=self.parse)

    # response
    def parse(self, response: scrapy.http.response.html.HtmlResponse):
        quote: scrapy.selector.unified.Selector
        for quote in response.selector.xpath("//div[@class='quote']"):
            loader = ItemLoader(item=QuoteItem(),
                                selector=quote,
                                response=response)
            loader.add_xpath('text', ".//div[@class='quoteText']/text()")
            loader.add_xpath('author', ".//span[@class='authorOrTitle']")
            loader.add_xpath('tags',
                             ".//div[@class='greyText smallText left']/a")
            yield loader.load_item()
            # yield {
            #     'text':
            #     quote.xpath(".//div[@class='quoteText']/text()[1]"
            #                 ).extract_first().strip(),
            #     'author':
            #     quote.xpath(".//span[@class='authorOrTitle']/text()").
            #     extract_first().strip(),
            #     'tags':
            #     quote.xpath(".//div[@class='greyText smallText left']/a/text()"
            #                 ).extract()
            # }

        next_page = response.selector.xpath(
            '//a[@class="next_page"]/@href').extract_first()
        if next_page:
            next_page_url = response.urljoin(next_page)
            yield scrapy.Request(url=next_page_url, callback=self.parse)
