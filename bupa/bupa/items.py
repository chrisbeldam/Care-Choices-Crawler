# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class BupaItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    url = scrapy.Field()
    home_title = scrapy.Field()
    description = scrapy.Field()
    address = scrapy.Field()
    pass

class ExtraCareItem(scrapy.Item):
    url = scrapy.Field()
    housing_name = scrapy.Field()
    address = scrapy.Field()
    telephone = scrapy.Field()
    cqc_id = scrapy.Field()
    care_provider = scrapy.Field()
    pass

class ExtraCareCCItem(scrapy.Item):
    pass

class DayCareCCItem(scrapy.Item):
    pass