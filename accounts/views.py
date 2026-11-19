from django.shortcuts import render, redirect
from .forms import RegistrationForm
from .models import Profile
from django.contrib.auth.decorators import login_required

from .forms import RegistrationForm
from .models import Profile


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
def dashboard(request):

    return render(request, 'accounts/dashboard.html')
