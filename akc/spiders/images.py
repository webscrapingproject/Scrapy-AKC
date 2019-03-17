# -*- coding: utf-8 -*-
import scrapy
from akc.items import ImageItem

class ImagesSpider(scrapy.Spider):
    name = 'images'
    allowed_domains = ['www.akc.org']
    start_urls = ['http://www.akc.org/dog-breeds/']

    def parse(self, response):
        # 去除第一个无意义选项
        options=response.css('.custom-select__select > option::attr(value)').extract()[1:]
        # names=response.css('.custom-select__select > option::text').extract()[1:]
        for item in options:
            yield scrapy.Request(item+'pictures/', callback=self.parse_detail)

    def parse_detail(self,response):
        # 图片名称
        title=response.css('#page-title > h1::text').extract_first().replace(' Image Gallery','')
        alt=response.css('.image-grid__item >.media-wrap > img::attr(alt)').extract()
        url=response.css('.image-grid__item >.media-wrap > img::attr(data-src)').extract()
        for i in range(len(alt)):
            item = ImageItem()
            item['id'] = alt[i]
            item['url'] = url[i]
            item['title'] = title
            item['image_name'] = '%s/%s.jpg' % (item['title'], item['id'])
            yield item


