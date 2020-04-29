# -*- coding: utf-8 -*-
import scrapy

page_num=2
class AmazonScrap2Spider(scrapy.Spider):
    name = 'amazon_scrap2'

    start_urls = ['https://www.amazon.com/s?i=specialty-aps&srs=17276810011&qid=1588150674&swrs=AF5B754DFF2FAA8BDA238ACC35626D8C&ref=sr_pg_1']
    def parse(self, response):
        global page_num
        div=response.css("div.s-include-content-margin.s-border-bottom.s-latency-cf-section")
        for i in div:
            book_name=i.css("span.a-size-medium.a-color-base.a-text-normal::text").extract()
            author_name=i.css("div.a-row.a-size-base.a-color-secondary a.a-size-base.a-link-normal::text").extract()
            price=i.css("span.a-price-whole::text").extract()
            yield {'product':book_name,'author':author_name,'price':price}
        next_page="https://www.amazon.com/s?i=specialty-aps&srs=17276810011&page="+str(page_num)+"&qid=1588153458&swrs=AF5B754DFF2FAA8BDA238ACC35626D8C&ref=sr_pg_"+str(page_num)
        page_num=page_num+1
        if page_num<=11:
            yield response.follow(next_page,callback=self.parse)