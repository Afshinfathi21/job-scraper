from django.urls import path
from jobs.views import JobListView,SkillListView

urlpatterns = [
    path('jobs/',JobListView.as_view(),name='jobs-list'),
    path('skills/',SkillListView.as_view(),name='skills-list')
]
