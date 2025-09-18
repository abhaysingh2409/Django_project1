from django.urls import path
from . import views

urlpatterns = [
    path('', views.student_list, name='student-list'),
    path('add/', views.student_add, name='student-add'),
    path('<int:pk>/', views.student_detail, name='student-detail'),
    path('<int:pk>/edit/', views.student_edit, name='student-edit'),
    path('<int:pk>/delete/', views.student_delete, name='student-delete'),
]