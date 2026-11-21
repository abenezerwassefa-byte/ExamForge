from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.db import transaction
from django.http import HttpResponseForbidden

from .forms import RegistrationForm
from .models import Profile, School, SchoolAdmin, Instructor

import os
import pyotp


def register(request):

    if request.method == 'POST':
        form = RegistrationForm(request.POST)

        if form.is_valid():
            user = form.save()
            Profile.objects.create(user=user)

            return redirect('login')

    else:
        form = RegistrationForm()

    return render(request, 'accounts/register.html', {'form': form})


@login_required
def student_dashboard(request):

    return render(request, 'accounts/student_dashboard.html')


def student_register(request):
    return render(request, 'accounts/student_register.html')


def instructor_register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)

        if form.is_valid():
            user = form.save()

            Profile.objects.create(
                user=user,
                role='instructor'
            )

            return redirect('login')

    else:
        form = RegistrationForm()
    return render(request, 'accounts/instructor_register.html', {'form': form})


def authentication(request):

    if request.method == 'POST':

        code = request.POST.get('totp_code', '').strip()
        secret = os.getenv('PLATFORM_ADMIN_TOTP_SECRET')

        if not secret:
            return render(request, 'accounts/authentication.html', {
                'error': 'Authorization is currently unavailable.'
            })

        totp = pyotp.TOTP(secret)

        if code.isdigit() and len(code) == 6 and totp.verify(code, valid_window=1):

            request.session['school_admin_authorized'] = True
            request.session.set_expiry(1200)

            return redirect('school_admin_register')

        return render(request, 'accounts/authentication.html', {
            'error': 'Invalid authentication code. Please try again.'
        })

    return render(request, 'accounts/authentication.html')


@login_required
def instructor_dashboard(request):
    profile = getattr(request.user, 'profile', None)

    if profile is None or profile.role != 'instructor':
        return HttpResponseForbidden(
            'You do not have permission to access this page.'
        )
    instructor_profiles = Instructor.objects.filter(
        user=request.user
    ).select_related('school')

    return render(request, 'accounts/instructor_dashboard.html', {
        'instructor_profiles': instructor_profiles
    })


@login_required
def school_admin_dashboard(request):

    profile = getattr(request.user, 'profile', None)

    if profile is None or profile.role != 'school admin':
        return HttpResponseForbidden(
            "You do not have permission to access this page."
        )

    return render(request, 'accounts/school_admin_dashboard.html', {'school': profile.school
                                                                    })


def school_admin_register(request):

    # 1. Verify Platform Administrator authorization.
    if not request.session.get('school_admin_authorized'):
        return redirect('school-admin-register')

    # 2. Process submitted registration data.
    if request.method == 'POST':

        school_name = request.POST.get('school_name', '').strip()
        full_name = request.POST.get('full_name', '').strip()
        email = request.POST.get('email', '').strip()
        username = request.POST.get('username', '').strip()
        password = request.POST.get('password', '')
        confirm_password = request.POST.get('confirm_password', '')

        # 3. Validate required fields.
        if not all([school_name, full_name, email, username, password, confirm_password]):
            return render(request, 'accounts/school_admin_register.html', {
                'error': 'All fields are required.'
            })

        # 4. Confirm that both passwords match.
        if password != confirm_password:
            return render(request, 'accounts/school_admin_register.html', {
                'error': 'The passwords do not match.'
            })

        # 5. Check whether the username already exists.
        User = get_user_model()

        if User.objects.filter(username=username).exists():
            return render(request, 'accounts/school_admin_register.html', {
                'error': 'This username is already taken.'
            })

        # 6. Check whether the email is already registered.
        if User.objects.filter(email__iexact=email).exists():
            return render(request, 'accounts/school_admin_register.html', {
                'error': 'This email address is already registered.'
            })

        # 7. Create all related records in one transaction.
        with transaction.atomic():

            user = User.objects.create_user(
                username=username,
                email=email,
                password=password,
                first_name=full_name
            )

            school = School.objects.create(
                name=school_name
            )

            Profile.objects.create(
                user=user,
                role='school admin',
                school=school
            )

            SchoolAdmin.objects.create(
                user=user,
                school=school
            )

        # 8. Revoke the temporary registration authorization.
        request.session.pop('school_admin_authorized', None)

        # 9. Redirect to login.
        return redirect('login')

    # 10. Display the registration form.
    return render(request, 'accounts/school_admin_register.html')


@login_required
def dashboard_redirect(request):

    profile = getattr(request.user, 'profile', None)

    if request.user.is_superuser:
        return redirect('/admin/')

    if profile is None:
        return HttpResponseForbidden('No accoutn profile found.')

    if profile.role == 'instructor':
        return redirect('instructor_dashboard')

    if profile.role == 'school admin':
        return redirect('school_admin_dashboard')

    if profile.role == 'stuent':
        return redirect('student_dashboard')

    return HttpResponseForbidden('Unrecognized account role.')
