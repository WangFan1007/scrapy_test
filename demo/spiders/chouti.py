# -*- coding: utf-8 -*-
import scrapy


class ChoutiSpider(scrapy.Spider):
    name = 'chouti'
    allowed_domains = ['dig.chouti.com']
    start_urls = ['http://dig.chouti.com/']

    def parse(self, response):
        item_list = response.xpath('//div[@id="content-list"]/div[@class="item"]')
        f = open('news.log',mode='a+')
        for item in item_list:
            text = item.xpath('.//a/text()').extract_first()
            href = item.xpath('.//a/@href').extract_first()
            f.write(href + '\n')

        f.close()

        page_list = response.xpath('//div[@id="dig_lcpage"]//a/@href').extract()
        for page in page_list:
            from scrapy.http import Request
            page = 'https://dig.chouti.com' + page
            yield Request(url=page, callback=self.parse)
