from celery import shared_task
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from multiprocessing import Process
from scraper.scraper.spiders.jobvision_spider import JobvisionSpider
import sys,os



@shared_task
def run_jobvision_spider():
    process = CrawlerProcess(get_project_settings())
    print(get_project_settings())
    process.crawl(JobvisionSpider)
    process.start()
