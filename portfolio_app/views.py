from django.shortcuts import render
from .models import Project, Skill , Certificate , Contact_me , Experience


def home(request):
    projects = Project.objects.all()
    contacts = Contact_me.objects.all()
    skills = Skill.objects.all()
    context = {
        'projects': projects,
        'contacts': contacts,
        'skills': skills,
    }
    return render(request, 'portfolio/home.html', context)

def about(request):
    skills = Skill.objects.all()
    experiences = Experience.objects.all()
    context = {
        'skills': skills,
        'experiences' : experiences
    
    }
    return render(request,'portfolio/about.html', context)
 

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

def certificate(request):
    certificates = Certificate.objects.all()
    context = {
        'certificates': certificates,
    }
    return render(request,'portfolio/Certificate.html',context)

 