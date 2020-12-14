# -*- coding: utf-8 -*-
import scrapy


class AllglassesSpider(scrapy.Spider):
    name = 'allglasses'
    allowed_domains = ['www.glassesshop.com']
    start_urls = ['https://www.glassesshop.com/bestsellers']

    def parse(self, response):
        for glass in response.xpath("//div[@id='product-lists']/div"):
            yield{
                'Title' : glass.xpath("normalize-space(.//div[@class='p-title']/a/text())").get()
            }
