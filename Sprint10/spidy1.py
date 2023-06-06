#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import scrapy


class MySpider(scrapy.Spider):
    name = "spider1"

    def start_requests(self):
        urls = ['https://www.moratour.com','https://my.weezevent.com/o-son-do-camino-2023']
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    # Scrap Web Page and Save  Code in File
    # ==============================================================================        

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = f'moratour_copy.html'
        #filename = f'spyder-{page}.html'
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log(f'Saved file {filename}')"

