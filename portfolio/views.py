from django.shortcuts import render
from .models import Profile, Service, Skill, Experience, Project, Certification

def home(request):
    profile = Profile.objects.first()
    services = Service.objects.all()
    skills = Skill.objects.all()
    featured_projects = Project.objects.filter(is_featured=True)[:2]
    recent_experience = Experience.objects.order_by('-start_date')[:2]
    return render(request, 'portfolio/home.html', {
        'profile': profile,
        'services': services,
        'skills': skills,
        'featured_projects': featured_projects,
        'recent_experience': recent_experience,
    })

def experience(request):
    profile = Profile.objects.first()
    experiences = Experience.objects.all().order_by('-start_date')
    return render(request, 'portfolio/experience.html', {
        'profile': profile,
        'experiences': experiences,
    })

def projects(request):
    profile = Profile.objects.first()
    projects = Project.objects.all().order_by('-year')
    categories = Project.objects.values_list('category', flat=True).distinct()
    return render(request, 'portfolio/projects.html', {
        'profile': profile,
        'projects': projects,
        'categories': categories,
    })

def certifications(request):
    profile = Profile.objects.first()
    certifications = Certification.objects.all().order_by('-issue_date')
    issuers = Certification.objects.values_list('issuer', flat=True).distinct()
    return render(request, 'portfolio/certifications.html', {
        'profile': profile,
        'certifications': certifications,
        'issuers': issuers,
    })
