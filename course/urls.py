
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CourseView

app_name = 'course'
routers = DefaultRouter()
routers.register('course',CourseView)

urlpatterns = [
    path('',include(routers.urls))
]