# -*- coding: utf-8 -*-
import scrapy
from dangdang.items import DangdangItem
from scrapy.http import Request
class DdSpider(scrapy.Spider):
    name = 'dd'
    allowed_domains = ['dangdang.com']
    start_urls = ['http://category.dangdang.com/pg1-cid4008154.html']

    def parse(self, response):
        item=DangdangItem()
        item["title"]=response.xpath("//a[@name='itemlist-title']/@title").extract()
        item["link"]=response.xpath("//a[@name='itemlist-title']/@href").extract()
        item["comment"]=response.xpath("//a[@name='itemlist-review']/text()").extract()
        # print(item["title"])
        yield item
        for i in range(2,11): #爬取2~10页
            url='http://category.dangdang.com/pg'+str(i)+'-cid4008154.html'
            yield Request(url, callback=self.parse)
