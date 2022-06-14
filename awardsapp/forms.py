from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile, Project


class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]


class UpdateProfileForm(forms.ModelForm):
    photo = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control-file'}))
    bio = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5}))

    class Meta:
        model = Profile
        fields = ['photo', 'bio']


class PostProjectForm(forms.ModelForm):
    # category = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))
    # name = forms.TextInput(attrs={'class': 'form-control'})
    # description = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5, 'cols': 20}))
    # link = forms.URLField()
    # image = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control-file'}))

    class Meta:
        model = Project
        fields = ['category', 'name', 'description', 'link', 'image']
