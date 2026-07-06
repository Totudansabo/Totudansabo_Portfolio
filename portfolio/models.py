from django.db import models

class Profile(models.Model):
    full_name = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    summary = models.TextField()
    about_text = models.TextField()
    years_experience = models.IntegerField(default=10)
    projects_delivered = models.IntegerField(default=50)
    profile_image = models.ImageField(upload_to='profile/', null=True, blank=True)
    cv_file = models.FileField(upload_to='cv/', null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    phone = models.CharField(max_length=20, null=True, blank=True)
    linkedin = models.URLField(null=True, blank=True)
    twitter = models.URLField(null=True, blank=True)
    whatsapp = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.full_name

class Service(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    icon = models.CharField(max_length=50, help_text="Material symbol icon name")
    color_class = models.CharField(max_length=50, default='primary')

    def __str__(self):
        return self.title

class ServiceDetail(models.Model):
    service = models.ForeignKey(Service, related_name='details', on_delete=models.CASCADE)
    detail = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.service.title} - {self.detail}"

class Skill(models.Model):
    name = models.CharField(max_length=100)
    icon = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return self.name

class Experience(models.Model):
    job_title = models.CharField(max_length=255)
    company = models.CharField(max_length=255)
    company_logo = models.ImageField(upload_to='experience/', null=True, blank=True)
    start_date = models.CharField(max_length=50)
    end_date = models.CharField(max_length=50, default='PRESENT')
    description = models.TextField()
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.job_title} at {self.company}"

class ExperiencePoint(models.Model):
    experience = models.ForeignKey(Experience, related_name='points', on_delete=models.CASCADE)
    point = models.TextField()

    def __str__(self):
        return f"{self.experience.company} point"

class ExperienceTag(models.Model):
    experience = models.ForeignKey(Experience, related_name='tags', on_delete=models.CASCADE)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Project(models.Model):
    title = models.CharField(max_length=255)
    category = models.CharField(max_length=100)
    year = models.CharField(max_length=10)
    description = models.TextField()
    image = models.ImageField(upload_to='projects/')
    is_featured = models.BooleanField(default=False)
    link = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.title

class Certification(models.Model):
    name = models.CharField(max_length=255)
    issuer = models.CharField(max_length=255)
    issuer_logo = models.ImageField(upload_to='certifications/logos/', null=True, blank=True)
    issue_date = models.CharField(max_length=50)
    credential_id = models.CharField(max_length=255, null=True, blank=True)
    certificate_image = models.ImageField(upload_to='certifications/images/')
    pdf_file = models.FileField(upload_to='certifications/pdfs/', null=True, blank=True)

    def __str__(self):
        return self.name
