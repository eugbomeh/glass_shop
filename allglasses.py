# -*- coding: utf-8 -*-
import scrapy


class AllglassesSpider(scrapy.Spider):
    name = 'allglasses'
    allowed_domains = ['www.glassesshop.com/bestsellers']
    start_urls = ['https://http://www.glassesshop.com/bestsellers/']

    def parse(self, response):
        pass
