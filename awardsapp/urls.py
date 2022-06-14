from django.urls import path, include
from . import views

urlpatterns = [
   path('signup', views.sign_up),
   path('', views.home),
   path('projects', views.projects, name='home-projects'),
   path('profile', views.profile, name='users-profile'),
   path('post-project', views.post_project),
   path('search-project', views.search_project, name='search_project'),
   path('ratings/', include('star_ratings.urls', namespace='ratings')),

]
