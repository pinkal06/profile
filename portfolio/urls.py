from django.urls import path
from . import views

app_name = 'portfolio'

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('education/', views.education, name='education'),
    path('skills/', views.skills, name='skills'),
    path('projects/', views.projects, name='projects'),
    path('resume/', views.resume, name='resume'),
    path('resume/pdf/', views.resume_pdf, name='resume_pdf'),
    path('contact/', views.contact, name='contact'),
]
