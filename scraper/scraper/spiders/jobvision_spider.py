import scrapy
from ..items import JobItem

class JobvisionSpider(scrapy.Spider):
    name='jobvision'
    start_urls=['https://jobvision.ir/jobs/category/developer/']
    

    def parse(self,response):
        job_cards=response