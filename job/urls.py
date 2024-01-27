from django.urls import path
from .views import JobList

urlpatterns = [
    path('job/', JobList.as_view()),
]