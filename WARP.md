# WARP.md

This file provides guidance to WARP (warp.dev) when working with code in this repository.

## Common Commands

### Development Server
```bash
# Start development server
python manage.py runserver

# Start development server on specific port
python manage.py runserver 8080
```

### Database Operations
```bash
# Create migrations for model changes
python manage.py makemigrations

# Apply migrations
python manage.py migrate

# Create superuser for admin access
python manage.py createsuperuser

# Open Django shell
python manage.py shell
```

### Testing
```bash
# Run all tests
python manage.py test

# Run tests for specific app
python manage.py test students

# Run tests with verbosity
python manage.py test --verbosity=2

# Run specific test class
python manage.py test students.tests.StudentModelTest

# Run specific test method
python manage.py test students.tests.StudentModelTest.test_student_creation
```

### Static Files and Admin
```bash
# Collect static files (for production)
python manage.py collectstatic

# Check for common issues
python manage.py check
```

### Environment Setup
```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment (Windows)
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

## Architecture Overview

### Project Structure
This is a Django 5.2.6 web application following Django's MVT (Model-View-Template) pattern:

- **sms_project/**: Main Django project configuration
  - `settings.py`: Django configuration, includes crispy forms for Bootstrap 4 styling
  - `urls.py`: Root URL routing (currently only includes admin)
- **students/**: Core app containing the student management system
  - Three main models: Student, Course, and Enrollment with complex relationships

### Data Models Architecture

#### Core Models Relationship
The application uses a three-model architecture with the following relationships:

1. **Student Model**: Core student information with academic status tracking
   - Includes comprehensive student data (personal, academic, contact)
   - Has year level choices (Freshman through Graduate)
   - Tracks GPA and enrollment status

2. **Course Model**: Academic course information
   - Manages course details, credits, and instructor information
   - Organized by semester and year

3. **Enrollment Model**: Junction table linking students to courses
   - One-to-many relationship with both Student and Course
   - Handles grade calculations with automatic grade point conversion
   - Tracks enrollment status and attendance
   - Uses `unique_together` constraint to prevent duplicate enrollments

#### Key Model Features
- **Automatic GPA Calculation**: Enrollment model includes grade point conversion logic
- **Soft Constraints**: Uses choices fields for data integrity (gender, year level, grades)
- **Audit Fields**: All models include created_at/updated_at timestamps
- **Ordering**: Models have sensible default ordering (students by name, courses by code)

### Configuration Details
- **Database**: SQLite (easily configurable for PostgreSQL/MySQL in settings.py)
- **Forms**: Django Crispy Forms with Bootstrap 4 integration
- **Admin**: Django admin is enabled but models not yet registered
- **URL Routing**: Currently minimal - only admin URLs configured

### Development Status
This appears to be a foundational setup with:
- Complete model definitions with relationships
- Basic Django project structure
- Dependencies configured (Django, crispy forms)
- Missing: Views, templates, URL routing, admin registration, and frontend implementation

## Development Notes

### Adding New Models
When extending the data model:
- Follow the existing pattern of including `created_at`/`updated_at` fields
- Add appropriate `__str__` methods and `get_absolute_url` if creating detail views
- Use choices fields for constrained data (see existing GENDER_CHOICES, GRADE_CHOICES patterns)

### Model Relationships
- The Enrollment model serves as the junction between Students and Courses
- When adding new relationships, consider whether they should cascade on delete
- The `unique_together` constraint on Enrollment prevents duplicate course registrations

### Admin Interface
To expose models in Django admin, register them in `students/admin.py` using:
```python
from .models import Student, Course, Enrollment
admin.site.register(Student)
admin.site.register(Course) 
admin.site.register(Enrollment)
```

### Bootstrap Integration
The project uses django-crispy-forms with Bootstrap 4. When creating forms:
- Import and use `{% load crispy_forms_tags %}` in templates
- Use `{{ form|crispy }}` for automatic Bootstrap styling
- Configuration is already set in settings.py