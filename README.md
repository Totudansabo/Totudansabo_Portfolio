# Dynamic Portfolio Website

A dynamic portfolio website built with Django, featuring an admin panel for easy content management and a certificates section.

## Features

- **Dynamic Content:** Manage your profile, experience, education, and skills directly from the Django admin.
- **Certificates Section:** Show off your professional achievements with a dedicated certifications area.
- **Responsive Design:** Based on a premium minimalist design system with Glassmorphism elements.
- **Easy Deployment:** Configured for quick setup and local development.

## Project Structure

- `portfolio_project/`: Project configuration and settings.
- `portfolio/`: Main application containing models, views, and templates.
- `media/`: Directory for uploaded profile images, resumes, and certificates.
- `staticfiles/`: Directory for collected static files.

## Setup Instructions

1. **Install Dependencies:**
   ```bash
   pip install django Pillow
   ```

2. **Database Setup:**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

3. **Create Superuser:**
   ```bash
   python manage.py createsuperuser
   ```

4. **Load Initial Data (Optional):**
   ```bash
   python manage.py loaddata initial_data
   ```

5. **Run the Server:**
   ```bash
   python manage.py runserver
   ```

6. **Access the Admin Panel:**
   Go to `http://127.0.0.1:8000/admin/` and log in with your superuser credentials to start adding content.

## Models

- **Profile:** Personal information, bio, contact links, and resume.
- **Experience:** Professional work history.
- **Education:** Academic background.
- **Skill:** Core competencies and technical skills.
- **Certificate:** Professional certifications with optional image and credential URL.

## Author

**Salisu Shamsuddeen**
*Executive Project Coordination & IT Solutions*
