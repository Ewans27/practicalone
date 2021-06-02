import scrapy
from ..items import PracticaloneItem

class Books2Spider(scrapy.Spider):
    name = 'Books2'
    allowed_domains = ['books.toscrape.com']
    start_urls = ['http://books.toscrape.com/catalogue/sapiens-a-brief-history-of-humankind_996/index.html/']

    def parse(self, response):
                item=PracticaloneItem()
                item['title']=response.xpath('//*[@id="content_inner"]/article/div[1]/div[2]/h1').extract()
                item['price']=response.xpath('//*[@id="content_inner"]/article/div[1]/div[2]/p[1]').extract()
                return item
