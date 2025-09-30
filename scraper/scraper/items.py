# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ScraperItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class JobItem(scrapy.Item):
    title=scrapy.Field()
    company=scrapy.Field()
    location=scrapy.Field()
    salary=scrapy.Field()
    description=scrapy.Field()
    skills=scrapy.Field()
    posted_at=scrapy.Field()