# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from jobs.models import Job,Company,Skill
from datetime import datetime
from asgiref.sync import sync_to_async

class DjangoPipeline:
    async def process_item(self,item,spider):
        await self.save_job(item)
        return item
    @sync_to_async
    def save_job(self,item):
        company,_=Company.objects.get_or_create(name=item.get('company'))
        job=Job.objects.create(title=item.get('title'),company=company,location=item.get('location'),salary=item.get('salary'),description=item.get('description'),posted_at=item.get('posted_at') or None)
        for skill_name in item.get('skills',[]):
            skill_name=skill_name.strip()
            if skill_name:
                skill,_=Skill.objects.get_or_create(name=skill_name)
                job.skills.add(skill)
        job.save()