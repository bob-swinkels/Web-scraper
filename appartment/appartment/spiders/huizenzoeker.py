# -*- coding: utf-8 -*-
from scrapy import Spider
from scrapy.selector import Selector
import re

from appartment.items import AppartmentItem

class AppartmentSpider(Spider):
    name = "appartment"
    allowed_domains = ["huizenzoeker.nl"]
    start_urls = [
        "https://www.huizenzoeker.nl/huur/noord-holland/amsterdam/?so=2",
        "https://www.huizenzoeker.nl/huur/noord-brabant/breda/?so=2",
        "https://www.huizenzoeker.nl/huur/zuid-holland/delft/?so=2",
        "https://www.huizenzoeker.nl/huur/noord-brabant/s-hertogenbosch/?so=2",
        "https://www.huizenzoeker.nl/huur/zuid-holland/s-gravenhage/?so=2",
        "https://www.huizenzoeker.nl/huur/noord-brabant/eindhoven/?so=2",
        "https://www.huizenzoeker.nl/huur/overijssel/enschede/?so=2",
        "https://www.huizenzoeker.nl/huur/groningen/groningen/?so=2",
        "https://www.huizenzoeker.nl/huur/friesland/leeuwarden/?so=2",
        "https://www.huizenzoeker.nl/huur/zuid-holland/leiden/?so=2",
        "https://www.huizenzoeker.nl/huur/limburg/maastricht/?so=2",
        "https://www.huizenzoeker.nl/huur/gelderland/nijmegen/?so=2",
        "https://www.huizenzoeker.nl/huur/zuid-holland/rotterdam/?so=2",
        "https://www.huizenzoeker.nl/huur/noord-brabant/tilburg/?so=2",
        "https://www.huizenzoeker.nl/huur/utrecht/utrecht/?so=2"
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
        item['url'] = response.request.url
        
        try:
            raw_location = response.xpath("//*/p[@class='locatie']/text()").extract()
            location_string = re.sub(r'[^\w]', '', raw_location[0]) # Remove all the weird characters
            item['city'] = location_string[6:]
            item['postal_code'] = location_string[:6]
        except IndexError:
            print("Item has no adress, skipping this item.")
            return
            
        try:
            price_raw = response.xpath("//*/div[@class='prijs']/strong/text()").extract()
            item['price'] = re.sub(r'[^\d]', '', price_raw[0]) # Remove the euro and dot
        except IndexError:
            print("Item has no price, skipping this item.")
            return
        
        try:
            size_raw = response.xpath("//*/th[text()='Woonoppervlakte']/following::td[1]/text()").extract()
            item['size'] = re.sub(r'[^\d]', '', size_raw[0]) # Remove the m2
        except IndexError:
            print("Item has no area, skipping this item.")
            return
        
        try:
            item['rooms'] = response.xpath("//*/th[text()='Aantal kamers']/following::td[1]/text()").extract()[0]
        except IndexError:
            print("Item has no number of rooms, skipping this item.")
            return
        
        yield item