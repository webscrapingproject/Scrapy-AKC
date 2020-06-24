# -*- coding: utf-8 -*-
import scrapy
from akc.items import ImageItem
import re


class ImagesSpider(scrapy.Spider):
    name = 'images'
    allowed_domains = ['www.akc.org']
    start_urls = ['http://www.akc.org/dog-breeds/']

    def parse(self, response):
        # 去除第一个无意义选项
        options=response.css('.custom-select__select > option::attr(value)').extract()[1:]
        names=response.css('.custom-select__select > option::text').extract()[1:]
        for i in range(len(options)):
            yield scrapy.Request(options[i] + 'pictures/', callback = self.parse_detail, meta = {'name': names[i]})

    def parse_detail(self,response):
        # 图片名称
        alt=response.css('.image-grid__item >.media-wrap > img::attr(alt)').extract()
        url=response.css('.image-grid__item >.media-wrap > img::attr(data-src)').extract()
        for i in range(len(alt)):
            item = ImageItem()
            item['id'] = alt[i].strip().replace('.','')
            item['url'] = re.sub('-[0-9x]*.jpg','.jpg',url[i]) # 替换成更大的图片地址
            item['title'] = response.meta['name'] # 保存的文件夹名
            item['image_name'] = item['title'] + '/' + item['id'] + '.jpg' # 保存的文件名（包括路径）
            yield item


