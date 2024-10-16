from django.shortcuts import render
from .models import Project, Skill ,Contact_me

def home(request):
    projects = Project.objects.all()
    contacts = Contact_me.objects.all()
    context = {
        'projects': projects,
        'contacts': contacts
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
def contact(request):
    return render(request,'portfolio/contact.html')