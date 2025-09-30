from django.shortcuts import render
from rest_framework import generics,permissions
from jobs.serializers import JobSerializer,SkillSerializer
from jobs.models import Job,Skill


# Create your views here.
class JobListView(generics.ListAPIView):
    serializer_class=JobSerializer
    queryset=Job.objects.all()

class SkillListView(generics.ListAPIView):
    queryset=Skill.objects.all()
    serializer_class=SkillSerializer

