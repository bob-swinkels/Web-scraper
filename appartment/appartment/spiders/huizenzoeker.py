# -*- coding: utf-8 -*-
from scrapy import Spider
from scrapy.selector import Selector

from appartment.items import AppartmentItem

class AppartmentSpider(Spider):
    name = "appartment"
    allowed_domains = ["huizenzoeker.nl"]
    start_urls = [
        "https://www.huizenzoeker.nl/huur/zuid-holland/s-gravenhage/",
    ]
    
    def parse(self, response):
        questions = Selector(response).xpath("//*/td[contains(@class, 'info')][a != '']")
    
        for question in questions:
            item = AppartmentItem()
            item['title'] = question.xpath("a[contains(@class, 'titel')]/strong/text()").extract()
            item['url'] = question.xpath("a[contains(@class, 'titel')]/@href").extract()
            yield item
            
        for a in response.css('#paginator a.volgende'):
            yield response.follow(a, callback=self.parse)