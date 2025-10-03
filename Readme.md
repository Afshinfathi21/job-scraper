# Jobscraper

job-scraper is a web application that scrapes job postings from multiple sources, stores them in a structured database, and provides an API to query job listings.  
It is built with Django, Django REST Framework, Celery, Scrapy, Redis, and Postgres, all orchestrated with Docker.

---

## 🚀 Features
- Scrape job postings from external websites (e.g., jobvision, LinkedIn, etc.)
- Store jobs, companies, and skills in a normalized Postgres database
- Expose REST APIs for accessing job data (powered by Django REST Framework)
- Scheduled scraping tasks with Celery Beat
- Asynchronous background workers with Celery + Redis
- Dockerized setup for easy local development

---

## 📦 Project Structure
- jobintel/               # Django project (backend API)
- jobs/                   # Django app for jobs, companies, skills
- scraper/                # Scrapy project (spiders, pipelines)
- docker-compose.yml      # Orchestrates all services
- backend/Dockerfile      # Django & Celery image
- entrypoint.sh           # Startup script (runs migrations, etc.)
---

## 🛠️ Tech Stack
- Backend: Django, Django REST Framework
- Scraping: Scrapy
- Task Queue: Celery + Redis
- Database: Postgres
- Containerization: Docker & Docker Compose

---

## ⚙️ Installation

### 1. Clone the repository
git clone https://github.com/Afshinfathi21/job-scraper.git
### 2. Create .env file
DB_NAME=jobintel
DB_USER=myuser
DB_PASSWORD=mypassword
DB_HOST=db
DB_PORT=5432
REDIS_HOST=redis
### 3. Build and start containers
docker-compose up --build
### 4. Create a superuser (optional)
docker-compose exec backend python manage.py createsuperuser
Now the Django API is available at:  
👉 http://localhost:8000  

---

## 📡 Running Scrapers

### With Celery (scheduled)
- Celery Beat schedules spiders (e.g., every day at 6 AM)
- Celery Worker runs the tasks asynchronously

Start worker + beat together:
docker-compose up celery_worker celery_beat
---

## 📚 API Endpoints (Examples)

- GET /api/jobs/ → List all jobs  
- GET /api/jobs/?skill=python → Filter jobs by skill  
- GET /api/companies/ → List companies  
- GET /api/skills/ → List skills  

---

## 🐳 Available Services

- backend → Django + DRF
- celery_worker → Executes scraping tasks
- celery_beat → Scheduler (e.g., scrape every 6 AM)
- db → Postgres
- redis → Message broker for Celery

---

## ✅ TODO
- Add more job sources (LinkedIn, jobinja, etc.)
- Improve job deduplication logic
- Add frontend dashboard (React/Vue/Next.js)
- Deploy to cloud (Heroku, AWS, etc.)

---
