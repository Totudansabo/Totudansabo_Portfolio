from django.shortcuts import render
from .models import Profile, Experience, Education, Skill, Certificate

def index(request):
    profile = Profile.objects.first()
    experiences = Experience.objects.all()
    education = Education.objects.all()
    core_skills = Skill.objects.filter(skill_type='CORE')
    tech_skills = Skill.objects.filter(skill_type='TECH')
    certificates = Certificate.objects.all()

    context = {
        'profile': profile,
        'experiences': experiences,
        'education': education,
        'core_skills': core_skills,
        'tech_skills': tech_skills,
        'certificates': certificates,
    }
    return render(request, 'portfolio/index.html', context)
