# -*- coding: utf-8 -*-

import scrapy

class TwpresItem(scrapy.Item):
    link = scrapy.Field()
    title = scrapy.Field()
    date = scrapy.Field()
    text = scrapy.Field()
    pass
