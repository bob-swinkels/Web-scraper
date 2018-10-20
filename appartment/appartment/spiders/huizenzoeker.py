# -*- coding: utf-8 -*-
from scrapy import Spider
from scrapy.selector import Selector
import re

from appartment.items import AppartmentItem

class AppartmentSpider(Spider):
    name = "appartment"
    allowed_domains = ["huizenzoeker.nl"]
    start_urls = [
        "https://www.huizenzoeker.nl/huur/zuid-holland/s-gravenhage/",
    ]
    
    def parse(self, response):
        
        for a in response.css('a.titel'):
            if a is not None:
                yield response.follow(a, callback=self.parse_appartment)
            
        for a in response.css('#paginator a.volgende'):
            if a is not None:
                yield response.follow(a, callback=self.parse)
            
    def parse_appartment(self, response):
        item = AppartmentItem()
        
        raw_location = response.xpath("//*/p[@class='locatie']/text()").extract()
        print(">"*10, raw_location)
        location_string = re.sub(r'[^\w]', '', raw_location[0]) # Remove all the weird characters
        print(">"*10, location_string)
        item['city'] = location_string[6:]
        item['postal_code'] = location_string[:6]
        
        price_raw = response.xpath("//*/div[@class='prijs']/strong/text()").extract()
        item['price'] = re.sub(r'[^\d]', '', price_raw[0]) # Remove the euro and dot
        
        size_raw = response.xpath("//*/th[text()='Woonoppervlakte']/following::td[1]/text()").extract()
        item['size'] = re.sub(r'[^\d]', '', size_raw[0]) # Remove the m2
        
        item['rooms'] = response.xpath("//*/th[text()='Aantal kamers']/following::td[1]/text()").extract()
        
        yield item