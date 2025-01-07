from django.shortcuts import render
from .models import Project, Skill , Certificate

def home(request):
    projects = Project.objects.all()
    certificate = Certificate.objects.all()
    skills = Skill.objects.all()
    context = {
        'projects': projects,
        'contacts': certificate,
        'skills': skills,
    }
    return render(request, 'portfolio/home.html', context)

def about(request):
    return render(request,'portfolio/about.html')
 

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
def Certificate(request):
    return render(request,'portfolio/Certificate.html')