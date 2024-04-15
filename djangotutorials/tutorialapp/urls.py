from urllib.parse import urlparse
from django.urls import path, include
from . import views

urlpatterns = [
    path('base/', views.base, name='base'),
    path('', views.home, name='home'),
    path('students/', views.students, name='students'),
    path('teachers/', views.teachers, name='teachers'),
]