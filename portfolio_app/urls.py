from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about',views.about,name='about'),
    path('projects',views.project,name='project'),
    path('skills',views.skill,name='skill'),
    path('certificate',views.Certificate,name='certificate')
]