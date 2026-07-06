from django.urls import path
from . import views

app_name = 'portfolio'

urlpatterns = [
    path('', views.home, name='home'),
    path('experience/', views.experience, name='experience'),
    path('projects/', views.projects, name='projects'),
    path('certifications/', views.certifications, name='certifications'),
]
