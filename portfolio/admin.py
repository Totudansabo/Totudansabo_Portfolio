from django.contrib import admin
from .models import Profile, Service, ServiceDetail, Skill, Experience, ExperiencePoint, ExperienceTag, Project, Certification

class ServiceDetailInline(admin.TabularInline):
    model = ServiceDetail
    extra = 1

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    inlines = [ServiceDetailInline]

class ExperiencePointInline(admin.TabularInline):
    model = ExperiencePoint
    extra = 1

class ExperienceTagInline(admin.TabularInline):
    model = ExperienceTag
    extra = 1

@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    inlines = [ExperiencePointInline, ExperienceTagInline]

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    pass

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    pass

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'year', 'is_featured')
    list_filter = ('category', 'is_featured')

@admin.register(Certification)
class CertificationAdmin(admin.ModelAdmin):
    list_display = ('name', 'issuer', 'issue_date')
