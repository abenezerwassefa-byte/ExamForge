from django.shortcuts import render, redirect
from .forms import RegistrationForm
from .models import Profile
from django.contrib.auth.decorators import login_required


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
    return render(request, 'accounts/instructor_register.html')


def school_admin_register(request):
    return render(request, 'accounts/school_admin_register.html')


def instructor_dashboard(request):
    return render(request, 'accounts/instructor_dashboard.html')


def school_admin_dashboard(request):
    return render(request, 'accounts/school_admin_dashboard.html')
