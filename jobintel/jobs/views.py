from django.shortcuts import render
from rest_framework import generics,permissions,viewsets,filters
from jobs.serializers import JobSerializer,SkillSerializer,CompanySerializer
from jobs.models import Job,Skill,Company
from django_filters.rest_framework import DjangoFilterBackend


# Create your views here.
class JobListView(viewsets.ModelViewSet):
    serializer_class=JobSerializer
    queryset=Job.objects.all()
    filter_backends=[DjangoFilterBackend,filters.SearchFilter,filters.OrderingFilter]
    filterset_fields=['company','location']
    search_fields=['title','salary','location']
    ordering_fields=['title','posted_at','company']
    def get_permissions(self):
        if self.request.method in ['POST','PATCH','DELETE','PUT']:
            return [permissions.IsAdminUser()]
        return [permissions.AllowAny()]


class SkillListView(generics.ListAPIView):
    queryset=Skill.objects.all()
    serializer_class=SkillSerializer

class CompanyListView(generics.ListAPIView):
    queryset=Company.objects.all()
    serializer_class=CompanySerializer

