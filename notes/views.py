from django.shortcuts import render, redirect

# Create your views here.


def home_view(request):
    if request.method == 'GET':
        return render(request, 'statics/home.html')
    else:
        return redirect('users/register')
