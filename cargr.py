# -*- coding: utf-8 -*-
import scrapy

# TODO how to mine data from car.gr? What kind of info would one want ? 
# PRICE ALERT
# car/spare part availability
# monitor specific sellers, try to offer advice to the customer
# how long does a ad stay up ?

class CargrScrapper(scrapy.Spider):

    def parse(self, response):
        scrapy.Spider.parse(self, response)



