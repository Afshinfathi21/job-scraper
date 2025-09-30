# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from jobs.models import Job,Company,Skill
from datetime import datetime

class DjangoPipeline:
    def process_item(self,item,spider):
        company,_=Company.objects.get_or_create(name=item.get('company'))
        job=Job.objects.create(title=item.get('title'),company=company,location=item.get('location'),salary=item.get('salary'),description=item.get('description'),posted_at=item.get('posted_at') or None)
        for skill_name in item.get('skills',[]):
            skill=Skill.objects.get(name=skill_name.strip())
            job.skills.add(skill)
        job.save()
        return item
