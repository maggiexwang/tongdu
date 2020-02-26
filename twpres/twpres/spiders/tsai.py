# -*- coding: utf-8 -*-
import sys
sys.path.append("C:/Users/xiaon/OneDrive/Thesis/tongdu/twpres/twpres")

import scrapy
from items import TwpresItem

class TsaiSpider(scrapy.Spider):
    name = 'tsai'
    allowed_domains = ['president.gov.tw']
    start_urls = ['https://www.president.gov.tw/Issue/72',
    'https://www.president.gov.tw/Issue/72/2/',
    'https://www.president.gov.tw/Issue/72/3/',
    'https://www.president.gov.tw/Issue/72/4/',
    'https://www.president.gov.tw/Issue/72/5/',
    'https://www.president.gov.tw/Issue/72/6/',
    'https://www.president.gov.tw/Issue/72/7/',
    'https://www.president.gov.tw/Issue/72/8/',
    'https://www.president.gov.tw/Issue/72/9/',
    'https://www.president.gov.tw/Issue/72/10/',
    'https://www.president.gov.tw/Issue/72/11']

    def parse(self, response):
    #def parse_links(self, response):
        base_absolute = 'https://www.president.gov.tw'
        for link in response.xpath("//a[starts-with(@href,'/NEWS/') and not(@title='兩岸')]/@href").getall():
            absolute_link = base_absolute + link
            yield scrapy.Request(absolute_link, callback=self.parse_page)
    
    def parse_page(self, response):
        item = TwpresItem()
        item['link'] = response.url
        item['title'] = response.xpath("//span[@style='font-weight:700;font-size:150%']/text()").get()
        item['date'] = response.xpath("//span[@class='date_green']/text()").get()
        item['text'] = response.xpath('//p/text()').getall()
        yield item