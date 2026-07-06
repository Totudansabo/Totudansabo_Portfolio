# Executive Digital Portfolio - Salisu Shamsuddeen

A high-end, executive-grade digital portfolio built with Django and Tailwind CSS, featuring a dynamic CMS-like admin interface.

## Features

- **Dynamic Content:** All information (Profile, Experience, Projects, Certifications, etc.) is manageable via the Django Admin.
- **Executive Design:** Apple-inspired minimalism with glassmorphism effects and sophisticated typography.
- **Responsive Layout:** Fully optimized for all screen sizes.
- **Search and Filters:** Interactive project and certification filtering.
- **CMS Ready:** Easy for non-technical users to update their portfolio through the secure admin dashboard.

## Tech Stack

- **Backend:** Django 6.0
- **Frontend:** Tailwind CSS (via CDN), Inter Font, Material Symbols
- **Database:** SQLite (default)
- **Environment:** `python-dotenv` for configuration

## Setup Instructions

### 1. Clone the Repository
```bash
git clone <repository-url>
cd <repository-directory>
```

### 2. Create and Activate Virtual Environment
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables
Create a `.env` file in the root directory:
```env
SECRET_KEY="your-secret-key"
DEBUG=True
ALLOWED_HOSTS="*"
```

### 5. Run Migrations
```bash
python manage.py migrate
```

### 6. Load Initial Data
```bash
python manage.py loaddata initial_data
```

### 7. Create Superuser (Admin Access)
```bash
python manage.py createsuperuser
```

### 8. Run Development Server
```bash
python manage.py runserver 0.0.0.0:3000
```
Visit `http://localhost:3000` to view the portfolio and `http://localhost:3000/admin` to access the dashboard.

## Project Structure

- `portfolio/`: Main application containing models, views, and templates.
- `portfolio_project/`: Project configuration and settings.
- `templates/`: Global templates (optional, most are in `portfolio/templates/`).
- `static/` & `staticfiles/`: Static assets management.
- `media/`: User-uploaded files (images, PDFs, CVs).

## Author

**Salisu Shamsuddeen** - *Executive Portfolio*
