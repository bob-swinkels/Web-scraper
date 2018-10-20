# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Item, Field

class AppartmentItem(Item):
    city = Field()
    postal_code = Field()
    price = Field()
    size = Field()
    rooms = Field()