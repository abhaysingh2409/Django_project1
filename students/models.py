from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Course(models.Model):
    """Model representing a course"""
    name = models.CharField(max_length=200)
    code = models.CharField(max_length=20, unique=True)
    description = models.TextField(blank=True)
    credits = models.PositiveIntegerField(default=3)
    instructor = models.CharField(max_length=200)
    semester = models.CharField(max_length=50)
    year = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['code']

    def __str__(self):
        return f"{self.code} - {self.name}"

    def get_absolute_url(self):
        return reverse('course-detail', kwargs={'pk': self.pk})


class Student(models.Model):
    """Model representing a student"""
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]
    
    YEAR_LEVEL_CHOICES = [
        ('1', 'Freshman'),
        ('2', 'Sophomore'),
        ('3', 'Junior'),
        ('4', 'Senior'),
        ('G', 'Graduate'),
    ]

    student_id = models.CharField(max_length=20, unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15, blank=True)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    address = models.TextField(blank=True)
    year_level = models.CharField(max_length=1, choices=YEAR_LEVEL_CHOICES)
    major = models.CharField(max_length=100)
    gpa = models.DecimalField(max_digits=3, decimal_places=2, default=0.00)
    enrollment_date = models.DateField()
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['last_name', 'first_name']

    def __str__(self):
        return f"{self.student_id} - {self.first_name} {self.last_name}"

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def get_absolute_url(self):
        return reverse('student-detail', kwargs={'pk': self.pk})


class Enrollment(models.Model):
    """Model representing student enrollment in a course"""
    GRADE_CHOICES = [
        ('A+', 'A+'),
        ('A', 'A'),
        ('A-', 'A-'),
        ('B+', 'B+'),
        ('B', 'B'),
        ('B-', 'B-'),
        ('C+', 'C+'),
        ('C', 'C'),
        ('C-', 'C-'),
        ('D+', 'D+'),
        ('D', 'D'),
        ('F', 'F'),
        ('I', 'Incomplete'),
        ('W', 'Withdrawn'),
        ('P', 'Pass'),
        ('NP', 'No Pass'),
    ]

    STATUS_CHOICES = [
        ('E', 'Enrolled'),
        ('D', 'Dropped'),
        ('C', 'Completed'),
        ('W', 'Withdrawn'),
    ]

    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    enrollment_date = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='E')
    grade = models.CharField(max_length=2, choices=GRADE_CHOICES, blank=True, null=True)
    grade_points = models.DecimalField(max_digits=3, decimal_places=2, null=True, blank=True)
    attendance_percentage = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ['student', 'course']
        ordering = ['-enrollment_date']

    def __str__(self):
        return f"{self.student.full_name} - {self.course.name}"

    def save(self, *args, **kwargs):
        """Auto-calculate grade points based on grade"""
        grade_points_map = {
            'A+': 4.00, 'A': 4.00, 'A-': 3.67,
            'B+': 3.33, 'B': 3.00, 'B-': 2.67,
            'C+': 2.33, 'C': 2.00, 'C-': 1.67,
            'D+': 1.33, 'D': 1.00, 'F': 0.00
        }
        if self.grade in grade_points_map:
            self.grade_points = grade_points_map[self.grade]
        super().save(*args, **kwargs)
