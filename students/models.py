from django.db import models
from django.urls import reverse


class Student(models.Model):
    """Simple Student model for student management system"""
    name = models.CharField(max_length=200)
    roll_number = models.CharField(max_length=20, unique=True)
    email = models.EmailField(unique=True)
    marks = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['roll_number']

    def __str__(self):
        return f"{self.roll_number} - {self.name}"

    def get_absolute_url(self):
        return reverse('student-detail', kwargs={'pk': self.pk})
