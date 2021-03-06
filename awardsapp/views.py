from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import RegisterForm, UpdateProfileForm, PostProjectForm
from .models import Project, Profile
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import ProjectSerializer, ProfileSerializer


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
    projects = Project.projects()
    return render(request, 'main/home.html', {"projects": projects})


def projects(request):
    projects = Project.projects()
    context = {
         "projects": projects,
    }
    return render(request, 'main/projects.html', context)


# def projects(request):
#     category = request.GET.get('category')
#     if category == None:
#         projects = Project.projects()
#     else:
#         projects = Project.search_project_by_category(category)
#     # categories = Category.objects.all()
#     context = {
#         "projects": projects,
#         # "categories": categories
#     }
#     return render(request, 'main/projects.html', context)


def profile(request):
    projects = request.user.profile.projects.all()
    if request.method == 'POST':
        profile_form = UpdateProfileForm(request.POST, request.FILES, instance=request.user.profile)

        if profile_form.is_valid():
            profile_form.save()
            messages.success(request, 'Your profile is updated successfully')
            return redirect(to='users-profile')
    else:
        profile_form = UpdateProfileForm(instance=request.user.profile)
    context = {
        "projects": projects,
        'profile_form': profile_form
    }
    return render(request, 'main/view_profile.html', context)


def post_project(request):
    if request.method == 'POST':
        form = PostProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.author = request.user.profile
            project.save()
            return redirect('home-projects')
    else:
        form = PostProjectForm()
    context = {
        'form': form
    }
    return render(request, 'main/post_project.html', context)


def search_project(request):
    if 'search-projects' in request.GET and request.GET['search-projects']:
        name = request.GET.get('search-projects')
        results = Project.search_project_by_category(name)
        message = name
        params = {
            'results': results,
            'message': message
        }
        return render(request, 'main/results.html', params)
    else:
        message = 'You did not make any selection'
    return render(request, 'main/results.html', {'message': message})


class ProjectList(APIView):
    def get(self, request, format=None):
        all_projects = Project.objects.all()
        serializers = ProjectSerializer(all_projects, many=True)
        return Response(serializers.data)


class ProfileList(APIView):
    def get(self, request, format=None):
        all_profiles = Profile.objects.all()
        serializers = ProfileSerializer(all_profiles, many=True)
        return Response(serializers.data)
