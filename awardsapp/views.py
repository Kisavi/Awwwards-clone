from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import RegisterForm, UpdateProfileForm, PostProjectForm
from .models import Project


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
    projects = Project.projects()
    context = {"projects": projects}
    return render(request, 'main/projects.html', context)


def profile(request):
    if request.method == 'POST':
        profile_form = UpdateProfileForm(request.POST, request.FILES, instance=request.user.profile)

        if profile_form.is_valid():
            profile_form.save()
            messages.success(request, 'Your profile is updated successfully')
            return redirect(to='users-profile')
    else:
        profile_form = UpdateProfileForm(instance=request.user.profile)
    return render(request, 'main/view_profile.html', {'profile_form': profile_form})


def post_project(request):
    project_form = PostProjectForm()
    return render(request, 'main/post_project.html', {'project_form': project_form})
