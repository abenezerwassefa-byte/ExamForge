from . import views
from django.urls import path

urlpatterns = [
    path('', views.register, name='accounts_home'),
    path('register/', views.register, name='register'),

    path('student-dashboard/', views.student_dashboard,
         name='student_dashboard'),

    path('register/student/', views.student_register,
         name='student_register'),

    path('register/instructor/', views.instructor_register,
         name='instructor_register'),

    path('instructor-dashboard/', views.instructor_dashboard,
         name='instructor_dashboard'),

    path('school-admin-dashboard/', views.school_admin_dashboard,
         name='school_admin_dashboard'),

    # School Administrator authorization
    path('school-admin-register/', views.authentication,
         name='school-admin-register'),

    # Actual registration form
    path('school-admin-register/form/', views.school_admin_register,
         name='school_admin_register'),
    path('dashboard/', views.dashboard_redirect, name='dashboard_redirect'),
]
