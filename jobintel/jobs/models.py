from django.db import models

# Create your models here.
class Company(models.Model):
    name=models.CharField(max_length=50,unique=True)
    website=models.URLField(max_length=200)
    def __str__(self):
        return self.name


class Skill(models.Model):
    name=models.CharField(max_length=50,unique=True)
    
    def __str__(self):
        return self.name

class Job(models.Model):
    title=models.CharField(max_length=250)
    company=models.ForeignKey(Company, on_delete=models.CASCADE)
    location=models.CharField(max_length=250,blank=True,null=True)
    salary=models.CharField(max_length=100,blank=True,null=True)
    description=models.TextField(blank=True,null=True)
    skills=models.ManyToManyField(Skill, blank=True)
    posted_at=models.DateTimeField(blank=True,null=True)
    scraped_at=models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f'{self.title} @ {self.company}'
