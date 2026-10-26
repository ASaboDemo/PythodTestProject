# DaCMS Python (Django)

This folder contains a Django-based Python port of the original ASP.NET Core CMS.

## What is covered

- Django project layout
- CMS entity models matching the core domain from the original .NET application
- admin registration for the main entities
- basic public-facing routes and template placeholders

## Quick start

1. Install Python 3.10+
2. Create a virtual environment
3. Install dependencies
4. Run migration and server

```bash
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

## Notes

This is a practical conversion scaffold. The original .NET project includes a larger set of controllers, filters, and localized Razor views. The Python version preserves the same domain model and app structure, but the remaining business logic can be ported as a second pass if full feature parity is needed.
