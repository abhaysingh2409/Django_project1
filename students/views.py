from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.db.models import Q
from django.http import JsonResponse
from .models import Student


def student_list(request):
    """Display all students with search functionality"""
    search_query = request.GET.get('search', '')
    
    if search_query:
        students = Student.objects.filter(
            Q(name__icontains=search_query) |
            Q(roll_number__icontains=search_query)
        )
    else:
        students = Student.objects.all()
    
    context = {
        'students': students,
        'search_query': search_query
    }
    return render(request, 'students/student_list.html', context)


def student_add(request):
    """Add a new student"""
    if request.method == 'POST':
        name = request.POST.get('name')
        roll_number = request.POST.get('roll_number')
        email = request.POST.get('email')
        marks = request.POST.get('marks')
        
        # Basic validation
        if not all([name, roll_number, email, marks]):
            messages.error(request, 'All fields are required!')
            return render(request, 'students/student_form.html')
        
        try:
            marks = float(marks)
            if marks < 0 or marks > 100:
                messages.error(request, 'Marks should be between 0 and 100!')
                return render(request, 'students/student_form.html')
        except ValueError:
            messages.error(request, 'Invalid marks value!')
            return render(request, 'students/student_form.html')
        
        # Check for duplicate roll number or email
        if Student.objects.filter(roll_number=roll_number).exists():
            messages.error(request, 'A student with this roll number already exists!')
            return render(request, 'students/student_form.html')
        
        if Student.objects.filter(email=email).exists():
            messages.error(request, 'A student with this email already exists!')
            return render(request, 'students/student_form.html')
        
        # Create student
        Student.objects.create(
            name=name,
            roll_number=roll_number,
            email=email,
            marks=marks
        )
        messages.success(request, 'Student added successfully!')
        return redirect('student-list')
    
    return render(request, 'students/student_form.html')


def student_edit(request, pk):
    """Edit an existing student"""
    student = get_object_or_404(Student, pk=pk)
    
    if request.method == 'POST':
        name = request.POST.get('name')
        roll_number = request.POST.get('roll_number')
        email = request.POST.get('email')
        marks = request.POST.get('marks')
        
        # Basic validation
        if not all([name, roll_number, email, marks]):
            messages.error(request, 'All fields are required!')
            return render(request, 'students/student_form.html', {'student': student})
        
        try:
            marks = float(marks)
            if marks < 0 or marks > 100:
                messages.error(request, 'Marks should be between 0 and 100!')
                return render(request, 'students/student_form.html', {'student': student})
        except ValueError:
            messages.error(request, 'Invalid marks value!')
            return render(request, 'students/student_form.html', {'student': student})
        
        # Check for duplicate roll number or email (excluding current student)
        if Student.objects.filter(roll_number=roll_number).exclude(pk=pk).exists():
            messages.error(request, 'A student with this roll number already exists!')
            return render(request, 'students/student_form.html', {'student': student})
        
        if Student.objects.filter(email=email).exclude(pk=pk).exists():
            messages.error(request, 'A student with this email already exists!')
            return render(request, 'students/student_form.html', {'student': student})
        
        # Update student
        student.name = name
        student.roll_number = roll_number
        student.email = email
        student.marks = marks
        student.save()
        
        messages.success(request, 'Student updated successfully!')
        return redirect('student-list')
    
    return render(request, 'students/student_form.html', {'student': student})


def student_delete(request, pk):
    """Delete a student"""
    student = get_object_or_404(Student, pk=pk)
    
    if request.method == 'POST':
        student.delete()
        messages.success(request, f'Student {student.name} deleted successfully!')
        return redirect('student-list')
    
    return render(request, 'students/student_confirm_delete.html', {'student': student})


def student_detail(request, pk):
    """View student details"""
    student = get_object_or_404(Student, pk=pk)
    return render(request, 'students/student_detail.html', {'student': student})
