from rest_framework import serializers
from .models import Project, Profile


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('user', 'bio', 'photo')


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ('author', 'category', 'name', 'link', 'pub_date', 'image', 'description')
