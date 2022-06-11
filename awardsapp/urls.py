from django.urls import path
from . import views

urlpatterns = [
   path('signup', views.sign_up),
   path('home', views.home),

]
