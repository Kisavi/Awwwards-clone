from django.urls import path
from . import views

urlpatterns = [
   path('signup', views.sign_up),
   path('', views.home),
   path('projects', views.projects),
   path('profile', views.profile, name='users-profile'),
   path('post-project', views.post_project),
   path('search-project', views.search_project, name='search-project'),

]
