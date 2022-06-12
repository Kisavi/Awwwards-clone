from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile', null=True)
    bio = models.CharField(max_length=300)
    photo = CloudinaryField('image',
                            default='http://res.cloudinary.com/dim8pysls/image/upload/v1639001486/x3mgnqmbi73lten4ewzv.png')

    def save_profile(self):
        self.save()

    @classmethod
    def get_profile_by_id(cls, id):
        profile = cls.objects.get(id=id)
        return profile

    @classmethod
    def update_profile(cls, prof):
        profile = cls.get_profile_by_id(prof.id)
        profile.bio = prof.bio
        profile.save_profile()

    def delete_profile(self):
        self.delete()

    def __str__(self):
        return self.bio


class Category(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)

    def save_category(self):
        self.save()

    @classmethod
    def get_category_by_id(cls, id):
        category = cls.objects.get(id=id)
        return category

    @classmethod
    def update_category(cls, cat):
        category = cls.get_category_by_id(cat.id)
        category.name = cat.name
        category.save_category()

    def delete_category(self):
        self.delete()

    def __str__(self):
        return self.name


class Project(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=100, null=False, blank=False)
    link = models.URLField(blank=False)
    pub_date = models.DateTimeField(auto_now_add=True)
    image = CloudinaryField(null=False, blank=False)
    description = models.TextField(max_length=500, null=False, blank=False)

    def save_project(self):
        self.save()

    def delete_project(self):
        self.delete()

    @classmethod
    def projects(cls):
        projects = cls.objects.all()
        return projects

    @classmethod
    def search_project_by_category(cls, category):
        projects = cls.objects.filter(category__name__icontains=category)
        return projects

    @classmethod
    def filter_by_category(cls, category):
        projects = cls.objects.filter(category__name__icontains=category)
        return projects

    def __str__(self):
        return self.category
