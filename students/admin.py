from django.contrib import admin
from .models import Student

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('roll_number', 'name', 'email', 'marks', 'created_at')
    list_filter = ('created_at', 'marks')
    search_fields = ('name', 'roll_number', 'email')
    ordering = ('roll_number',)
