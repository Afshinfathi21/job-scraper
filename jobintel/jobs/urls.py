from django.urls import path,include
from jobs.views import JobListView,SkillListView,CompanyListView
from rest_framework.routers import DefaultRouter

router=DefaultRouter()
router.register(r'jobs',JobListView,basename='jobs')

urlpatterns = [
    path("",include(router.urls)),
    path('skills/',SkillListView.as_view(),name='skills-list'),
    path('company/',CompanyListView.as_view(),name='company-list')
]
