# -*- coding: utf-8 -*-

import scrapy
from scrapy.shell import inspect_response
from scrapy.exporters import JsonLinesItemExporter as Exporter

# TODO how to mine data from car.gr? What kind of info would one want ?
# PRICE ALERT
# car/spare part availability
# monitor specific sellers, try to offer advice to the customer
# how long does a ad stay up ?


class CargrScrapper(scrapy.Spider):
    name = 'cargr'

    start_urls = ['https://www.car.gr/classifieds/cars/view/9172585/']

    def start_requests(self):
        request = scrapy.Request(self.start_urls[0] + '?lang=en') # TODO: how to pass params to url ?
        request.headers.update({'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36'})
        yield request

    def parse(self, response):
        # TODO: if ends with / put 1, else increment by 1
        # if response.ok != True skip page
        # extract the following
        export_file = open('cars.json', 'wb')
        exporter = Exporter(export_file)
        car = {}
        tag_tr_list = response.xpath("//table[1]//tr")
        for tr in tag_tr_list:
            _key = tr.xpath(".//td[1]/text()").extract()
            _value = tr.xpath(".//td[2]/span/text()").extract()
            #inspect_response(response, self)
            if not _value:
                _value = tr.xpath(".//td[2]/node()/text()").extract()
            if _key and _value:
                car.update({_key[0]: _value[0]})
        exporter.export_item(car)# TODO: utf should be decoded


