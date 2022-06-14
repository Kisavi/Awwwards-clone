from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import RegisterForm, UpdateProfileForm, PostProjectForm
from .models import Project, Category


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
    category = request.GET.get('category')
    if category == None:
        projects = Project.projects()
    else:
        projects = Project.search_project_by_category(category)
    categories = Category.objects.all()
    context = {
        "projects": projects,
        "categories": categories
    }
    return render(request, 'main/projects.html', context)


def profile(request):
    # projects = request.user.profile.projects.all()
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
    categories = Category.objects.all()
    if request.method == 'POST':
        project_form = PostProjectForm(request.POST, request.FILES)
        print('project_form:', project_form)
        if project_form.is_valid():
            print(Project.category.name)
            project = project_form.save(commit=False)
            project.author = request.user.profile
            project.save()
            return redirect('home-projects')
    else:
        project_form = PostProjectForm()
        params = {
            'categories': categories,
            'project_form': project_form
        }
    return render(request, 'main/post_project.html', params)


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
