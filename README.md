# Postscribers

Postscribers is a Django-based blogging platform where authenticated users can create posts, comment on posts, and manage their profiles (including profile images).

## Features

- User authentication (login/logout)
- User registration
- Password reset flow via email
- Create, edit, and delete blog posts
- Comment on individual posts
- Profile management with profile photo upload
- Django admin panel
- Static file serving with WhiteNoise
- Deployment configuration for Render

## Tech Stack

- Python
- Django 6
- SQLite (default local database)
- `dj-database-url` for flexible DB configuration
- `python-dotenv` for local environment variable loading
- `django-crispy-forms` + `crispy-bootstrap5` for form rendering
- WhiteNoise + Gunicorn for production hosting

## Project Structure

```text
postscribers/              # Django project configuration
blog/                      # Blog app (posts, comments, blog views)
users/                     # User app (signup, profile, auth-related views)
templates/                 # HTML templates
static/                    # Static assets
media/                     # Uploaded media (created at runtime)
manage.py
render.yaml                # Render deployment settings
requirements.txt
```

## Prerequisites

- Python 3.12+ (project is configured for Python 3.14.0 on Render)
- `pip`

## Installation

1. **Clone the repository**

   ```bash
   git clone <your-repo-url>
   cd django-blog
   ```

2. **Create and activate a virtual environment**

   ```bash
   python -m venv .venv
   source .venv/bin/activate  # macOS/Linux
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Create a `.env` file** in the project root:

   ```env
   SECRET_KEY=your-django-secret-key
   DEBUG=True
   EMAIL_HOST_USER=your-email@gmail.com
   EMAIL_PASSWORD=your-app-password
   ```

   Notes:
   - `SECRET_KEY` and `DEBUG` are read from environment variables.
   - Email settings are configured for Gmail SMTP.

5. **Run migrations**

   ```bash
   python manage.py migrate
   ```

6. **Create a superuser (optional, for admin access)**

   ```bash
   python manage.py createsuperuser
   ```

7. **Start the development server**

   ```bash
   python manage.py runserver
   ```

8. Visit:
   - App: `http://127.0.0.1:8000/`
   - Blog: `http://127.0.0.1:8000/blog/`
   - Admin: `http://127.0.0.1:8000/admin/`

## Environment Variables

| Variable | Required | Purpose |
|---|---|---|
| `SECRET_KEY` | Yes | Django secret key |
| `DEBUG` | Yes | Enables debug mode when set to `True` |
| `EMAIL_HOST_USER` | For password reset email | SMTP username |
| `EMAIL_PASSWORD` | For password reset email | SMTP password / app password |
| `DATABASE_URL` | Optional | Overrides default SQLite database |

## Authentication & Routes

- `/` → Login page
- `/sign_up/` → User registration
- `/logout/` → Logout
- `/profile/` → User profile
- `/blog/` → Blog feed + create post
- `/post_detail/<id>/` → Post detail + comments
- `/post_edit/<id>/` → Edit post
- `/post_delete/<id>/` → Delete post
- `/admin/` → Django admin