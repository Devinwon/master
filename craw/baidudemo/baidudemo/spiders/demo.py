# -*- coding: utf-8 -*-
import scrapy


class DemoSpider(scrapy.Spider):
    name = 'demo'
    # allowed_domains = ['baidu.com']
    start_urls = ['https://python123.io/ws/demo.html']

    def parse(self, response):
    	fname=response.url.split('/')[-1]
    	with open(fname,'wb') as f:
    		f.write(response.body)
    	self.log("saved file %s."%fname)
      
