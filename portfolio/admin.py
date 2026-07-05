from django.contrib import admin
from .models import Profile, Experience, Education, Skill, Certificate

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'title', 'email')

@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('job_title', 'company', 'start_date', 'end_date', 'order')
    list_editable = ('order',)

@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ('degree', 'institution', 'end_date')

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('name', 'skill_type', 'percentage', 'category')
    list_filter = ('skill_type',)

@admin.register(Certificate)
class CertificateAdmin(admin.ModelAdmin):
    list_display = ('title', 'issuing_organization', 'issue_date')
