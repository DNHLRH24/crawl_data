import scrapy
from ..items import WeatherItem #Tên của dự án + Item

class WeatherspiderSpider(scrapy.Spider):
    name = "weatherspider"
    allowed_domains = ["weaather.com"]
    start_urls = ["https://weather.com/vi-VN/weather/today/l/VMXX0006:1:VM?Goto=Redirected"]

def parse(self, response):
    cities = response.xpath('//span[@class="CurrentConditions--location--1YWj_"]/text()').getall()
    temperatures = response.xpath('//small[@class="TemperatureValue"]/text()').getall()

    for city, temperature in zip(cities, temperatures):
        item = WeatherItem()  # Tạo 1 đối tượng chứa dữ liệu
        item["city"] = city
        item["temperature"] = temperature
        yield item  # Lưu dữ liệu
    pass