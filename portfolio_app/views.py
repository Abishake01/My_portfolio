from django.shortcuts import render
from .models import Project, Skill , Certificate , Contact_me , Experience , Resume , Gallery


def home(request):
    projects = Project.objects.all()
    contacts = Contact_me.objects.all()
    skills = Skill.objects.all()
    resume = Resume.objects.filter(is_active=True).first()
    context = {
        'projects': projects,
        'contacts': contacts,
        'skills': skills,
        'resume': resume,
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

def resume(request):
 
    resume = Resume.objects.filter(is_active=True).first()
    if not resume:
        resume = Resume.objects.order_by('-uploaded_at').first()
    
    context = {
        'resume': resume,
    }
    return render(request, 'portfolio/resume.html', context)

def gallery(request):
    galleries = Gallery.objects.all()
    
    # Group by category
    hackathons = galleries.filter(category='hackathons')
    events = galleries.filter(category='events')
    personal = galleries.filter(category='personal')
    
    context = {
        'galleries': galleries,
        'hackathons': hackathons,
        'events': events,
        'personal': personal,
    }
    return render(request, 'portfolio/gallery.html', context)
