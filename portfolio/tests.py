from django.test import TestCase, Client
from django.urls import reverse
from .models import Profile, Service, Experience, Project, Certification

class PortfolioViewsTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.profile = Profile.objects.create(
            full_name="Salisu Shamsuddeen",
            title="Test Title",
            summary="Test Summary",
            about_text="Test About"
        )
        self.service = Service.objects.create(
            title="Test Service",
            description="Test Description",
            icon="hub"
        )
        self.experience = Experience.objects.create(
            job_title="Test Job",
            company="Test Company",
            start_date="2021",
            end_date="PRESENT"
        )
        self.project = Project.objects.create(
            title="Test Project",
            category="Test Category",
            year="2024",
            description="Test Description",
            image="projects/test.jpg"
        )
        self.cert = Certification.objects.create(
            name="Test Cert",
            issuer="Test Issuer",
            issue_date="2024",
            certificate_image="certs/test.jpg"
        )

    def test_home_view(self):
        response = self.client.get(reverse('portfolio:home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Salisu Shamsuddeen")

    def test_experience_view(self):
        response = self.client.get(reverse('portfolio:experience'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Job")

    def test_projects_view(self):
        response = self.client.get(reverse('portfolio:projects'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Project")

    def test_certifications_view(self):
        response = self.client.get(reverse('portfolio:certifications'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Cert")
