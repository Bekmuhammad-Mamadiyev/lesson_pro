from django.urls import path
from kompaniya.views import blogspage,homepage,resumepage



urlpatterns = [
    path('',homepage,name='home-page'),
    path('blogs/',blogspage,name='blogs-page'),
    path('resume/',resumepage,name='resume-page'),
]