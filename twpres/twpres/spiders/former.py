# -*- coding: utf-8 -*-
import sys
sys.path.append("C:/Users/xiaon/OneDrive/Thesis/tongdu/twpres/twpres")

import scrapy
from items import TwpresItem

class FormerSpider(scrapy.Spider):
    name = 'former'
    allowed_domains = ['president.gov.tw']
    
    #generate list of start_urls to avoid dealing with the tricky page flip
    #TW Office of the President website currently has 4082 pages in its news section
    base_url = 'https://www.president.gov.tw/Page/35/'
    url_list = []
    for i in range(1,4083):
        page = str(i)
        new_url = base_url + page + '/---S'
        url_list.append(new_url)
    start_urls = url_list

    def parse(self, response):
    #def parse_links(self, response):
        base_absolute = 'https://www.president.gov.tw'
        for link in response.xpath("//a[starts-with(@href,'/NEWS/')]/@href").getall():
            absolute_link = base_absolute + link
            yield scrapy.Request(absolute_link, callback=self.parse_page)
    
    def parse_page(self, response):
        item = TwpresItem()
        item['link'] = response.url
        item['title'] = response.xpath("//span[@style='font-weight:700;font-size:150%']/text()").get()
        item['date'] = response.xpath("//span[@class='date_green']/text()").get()
        item['text'] = response.xpath('//p/text()').getall()
        yield item