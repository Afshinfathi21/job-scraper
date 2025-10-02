from celery import shared_task
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from multiprocessing import Process
from scraper.scraper.spiders.jobvision_spider import JobvisionSpider

@shared_task
def run_jobvision_spider():
    # def _crawl():
    #     process = CrawlerProcess(get_project_settings())
    #     process.crawl(JobvisionSpider)
    #     process.start()
    process = CrawlerProcess(get_project_settings())
    process.crawl(JobvisionSpider)
    process.start()
    # p = Process(target=_crawl)
    # p.start()
    # p.join()