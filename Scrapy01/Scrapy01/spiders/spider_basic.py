import scrapy
from ..items import Scrapy01Item #Tên của dự án + Item

class SpiderBasicSpider(scrapy.Spider):
    name = "spider_basic"
    allowed_domains = ["quotes.toscrape.com"]
    start_urls = ["http://quotes.toscrape.com/"]

    def parse(self, response):
        reviews = response.xpath('//span[@class="text"]/text()').getall()

        authors = response.xpath('//small[@class="author"]/text()').getall()
        for review, author in zip(reviews, authors):
            item = Scrapy01Item() #Tạo 1 đối tượng chứa dữ liệu
            item["review"]=review
            item["author"]= author
            yield item #Lưu dữ liệu
        pass