import scrapy
from ..items import JobItem
import json


class JobvisionSpider(scrapy.Spider):
    name='jobvision'
    # start_urls=['https://candidateapi.jobvision.ir/api/v1/JobPost/List']

    def start_requests(self):
        url='https://candidateapi.jobvision.ir/api/v1/JobPost/List'
        payload={
            'jobCategoryUrlTitle':'developer',
            'pageSize':30,
            'requestedPage':1,
            'sortBy':1
        }
        headers={
            "Content-Type":"application/json; charset=utf-8",
            "User-Agent":"Mozilla/5.0"
        }

        yield scrapy.Request(
            url,
            method='POST',
            body=json.dumps(payload),
            headers=headers,
            callback=self.parse_api
        )

    def parse_api(self,response):
        data=json.loads(response.text)
        for job in data['data']['jobPosts']:
            job_id=job['id']
            url=f'https://candidateapi.jobvision.ir/api/v1/JobPost/Detail?jobPostId={job_id}'
            yield scrapy.Request(url,callback=self.parse_job)

    def parse_job(self,response):
        data=json.loads(response.text)
        skills=[]
        for skill in data['data']['jobCategories']:
            skills.append(skill['titleFa'])
        yield {
            'title':data['data']['title'],
            'description':data['data']['description'],
            'company':data['data']['company']['name']['titleFa'],
            'location':f'{data['data']['location']['province']['titleFa']},{data['data']['location']['city']['titleFa']}',
            'salary':data['data']['salary']['titleFa'],
            'skills':skills,
            'posted_at':data['data']['activationTime']['date']
        }