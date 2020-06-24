# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import os
from scrapy import Request
from scrapy.exceptions import DropItem
from scrapy.pipelines.images import ImagesPipeline



class ImagePipeline(ImagesPipeline):
    def file_path(self, request, response=None, info=None):
        folder='images'+'/'+request.meta['title']
        if not os.path.exists(folder):
            os.mkdir(folder)
        ## 在setting的IMAGES_STORE的sub directory
        image_path = request.meta['image_name']  # 路径 文件夹名字
        return image_path

    # 下载成功
    def item_completed(self, results, item, info):
        image_paths = [x['path'] for ok, x in results if ok]
        if not image_paths:
            raise DropItem('Image Downloaded Failed')
        return item

    # 爬取item对象
    def get_media_requests(self, item, info):
        yield Request(item['url'], meta={'title': item['title'],'image_name':item['image_name'], 'proxy':'http://127.0.0.1:8889'})


class AkcPipeline(object):
    def process_item(self, item, spider):
        return item