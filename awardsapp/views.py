from django.shortcuts import render, redirect
from .forms import RegisterForm


# Create your views here.

def sign_up(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/login')
    else:
        form = RegisterForm()
    return render(request, 'registration/signup.html', {'form': form})


def home(request):
    return render(request, 'main/home.html')


def projects(request):
    return render(request, 'main/projects.html')


def profile(request):
    return render(request, 'main/view_profile.html')


def post_project(request):
    return render(request, 'main/post_project.html')
