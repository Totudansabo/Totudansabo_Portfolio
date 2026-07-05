from django.db import models

class Profile(models.Model):
    full_name = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    bio = models.TextField()
    email = models.EmailField()
    linkedin = models.URLField(blank=True)
    github = models.URLField(blank=True)
    resume = models.FileField(upload_to='resumes/', blank=True)
    avatar = models.ImageField(upload_to='profile/', blank=True)

    def __str__(self):
        return self.full_name

class Experience(models.Model):
    job_title = models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    location = models.CharField(max_length=200, blank=True)
    start_date = models.CharField(max_length=100) # e.g., "2024" or "Jan 2024"
    end_date = models.CharField(max_length=100, default="PRESENT")
    is_current = models.BooleanField(default=False)
    description = models.TextField()
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['-order', '-id']

    def __str__(self):
        return f"{self.job_title} at {self.company}"

class Education(models.Model):
    degree = models.CharField(max_length=200)
    institution = models.CharField(max_length=200)
    details = models.CharField(max_length=200, blank=True) # e.g., "Second Class Upper"
    start_date = models.CharField(max_length=100, blank=True)
    end_date = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f"{self.degree} from {self.institution}"

class Skill(models.Model):
    SKILL_TYPE_CHOICES = [
        ('CORE', 'Core Competency'),
        ('TECH', 'Tech Skill'),
    ]
    name = models.CharField(max_length=100)
    percentage = models.IntegerField(default=0)
    skill_type = models.CharField(max_length=10, choices=SKILL_TYPE_CHOICES, default='CORE')
    category = models.CharField(max_length=100, blank=True) # e.g., "Advanced", "Infrastructure"

    def __str__(self):
        return self.name

class Certificate(models.Model):
    title = models.CharField(max_length=200)
    issuing_organization = models.CharField(max_length=200)
    issue_date = models.CharField(max_length=100, blank=True)
    credential_url = models.URLField(blank=True)
    image = models.ImageField(upload_to='certificates/', blank=True)

    def __str__(self):
        return self.title
