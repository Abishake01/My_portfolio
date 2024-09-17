from django.shortcuts import render
from .models import Project, Skill 

def home(request):
    projects = Project.objects.all()
     
    context = {
        'projects': projects,
    }
    return render(request, 'portfolio/home.html', context)
 

def project(request):
    projects = Project.objects.all()
    context = {
        'projects': projects,
    }
    return render(request,'portfolio/projects.html',context)
def skill(request):
    skills = Skill.objects.all()
    context = {
        'skills': skills,
    }
    return render(request,'portfolio/skills.html',context)