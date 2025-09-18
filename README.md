# Student Management System

A comprehensive web application built with Django for managing student information, courses, and enrollments.

## Features

- **Student Management**: Add, view, edit, and manage student profiles
- **Course Management**: Create and manage course information
- **Enrollment Tracking**: Track student enrollments in courses
- **Grade Management**: Record and manage student grades
- **User-friendly Interface**: Clean and responsive web interface using Bootstrap

## Models

### Student
- Student ID, Name, Email, Phone
- Date of Birth, Gender, Address
- Year Level, Major, GPA
- Enrollment Date and Status

### Course
- Course Name and Code
- Description, Credits
- Instructor Information
- Semester and Year

### Enrollment
- Student-Course relationships
- Enrollment status and dates
- Grade tracking with automatic GPA calculation
- Attendance percentage

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd student-management-system
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   # On Windows:
   venv\Scripts\activate
   # On macOS/Linux:
   source venv/bin/activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run migrations:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. Create a superuser (optional):
   ```bash
   python manage.py createsuperuser
   ```

6. Run the development server:
   ```bash
   python manage.py runserver
   ```

7. Visit `http://127.0.0.1:8000/` in your browser

## Project Structure

```
student-management-system/
├── sms_project/           # Main project directory
│   ├── __init__.py
│   ├── settings.py        # Django settings
│   ├── urls.py            # Main URL configuration
│   ├── wsgi.py            # WSGI configuration
│   └── asgi.py            # ASGI configuration
├── students/              # Students app
│   ├── migrations/        # Database migrations
│   ├── models.py          # Data models
│   ├── views.py           # View functions
│   ├── urls.py            # App URL configuration
│   ├── admin.py           # Django admin configuration
│   ├── apps.py            # App configuration
│   └── tests.py           # Tests
├── venv/                  # Virtual environment
├── manage.py              # Django management script
├── requirements.txt       # Python dependencies
├── db.sqlite3            # SQLite database
└── README.md             # This file
```

## Technologies Used

- **Backend**: Django 5.2.6
- **Database**: SQLite (default, easily configurable for PostgreSQL/MySQL)
- **Frontend**: HTML, CSS, Bootstrap 4
- **Forms**: Django Crispy Forms with Bootstrap 4

## Next Steps

To complete the application, you may want to add:

1. **Views and Templates**: Create CRUD views for students, courses, and enrollments
2. **Authentication**: Add user authentication and authorization
3. **API**: Create REST API endpoints using Django REST Framework
4. **Search and Filtering**: Add search and filter functionality
5. **Reports**: Generate academic reports and statistics
6. **File Uploads**: Add profile pictures and document uploads
7. **Email Notifications**: Send notifications for important events

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests
5. Submit a pull request

## License

This project is open source and available under the [MIT License](LICENSE).