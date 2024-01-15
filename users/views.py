from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import RegistrationForm
# Create your views here.


def registration_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            # Zmień 'home' na URL strony docelowej po zarejestrowaniu
            return redirect('home')
    else:
        form = RegistrationForm()
    return render(request, 'users/registration.html', {'form': form})
