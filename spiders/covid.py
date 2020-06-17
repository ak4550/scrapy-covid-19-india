# -*- coding: utf-8 -*-
import scrapy


class CovidSpider(scrapy.Spider):
    name = 'covid'
    allowed_domains = ['www.mygov.in']
    start_urls = ['https://www.mygov.in/corona-data/covid19-statewise-status/']

    def parse(self, response):
        state_names = response.xpath('//div[@class="field field-name-field-select-state field-type-list-text field-label-above"]/div[@class="field-items"]/div[@class="field-item even"]/text()').getall()
        confirmed_cases = response.xpath('//div[@class="field field-name-field-total-confirmed-indians field-type-number-integer field-label-above"]/div[@class="field-items"]/div[@class="field-item even"]/text()').getall()

        for i, v in enumerate(state_names):
            
            yield{
                "State" : v,
                "Confirmed Cases": confirmed_cases[i]
            }