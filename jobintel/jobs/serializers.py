from rest_framework import serializers
from jobs.models import Job,Company,Skill

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model=Company
        fields='__all__'
class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model=Skill
        fields='__all__'
class JobSerializer(serializers.ModelSerializer):
    company=CompanySerializer()
    skills=SkillSerializer(many=True)
    class Meta:
        model=Job
        fields='__all__'
