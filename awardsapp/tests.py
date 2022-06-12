from django.test import TestCase
from .models import Profile, Project, Category
from django.contrib.auth.models import User


# Create your tests here.

class CategoryTestCase(TestCase):
    """Test case for Category model"""

    def setUp(self):
        """Set up for the models instances"""
        self.category = Category(name='HTML')

    def tearDown(self):
        """Method to clear the model objects in the db after each testcase"""
        Category.objects.all().delete()

    def test_instance(self):
        """Test case to check if created category is an instance of Category model class"""
        self.assertTrue(isinstance(self.category, Category))

    def test_save_category(self):
        """Test case to check if created category is being saved in our database"""
        self.category.save_category()
        categories = Category.objects.all()
        self.assertTrue(len(categories) > 0)

    def test_get_category_by_id(self):
        """Test case to check we can access the id of a saved image in the database."""
        self.category.save_category()
        category = Category.get_category_by_id(self.category.id)
        self.assertTrue(category)

    def test_update_category(self):
        """Test case to check if a saved category is being updated successfully"""
        self.category.save_category()
        self.category.name = 'Food'
        Category.update_category(self.category)
        updated_category = Category.objects.get(id=self.category.id)
        self.assertEqual(updated_category.name, 'Food')

    def test_delete_category(self):
        """Test case to check if a saved category is being removed from our db when deleted."""
        self.category.save_category()
        self.category.delete_category()
        categories = Category.objects.all()
        self.assertTrue(len(categories) == 0)


class ProfileTestCase(TestCase):
    """Test case for Location model"""

    def setUp(self):
        """Set up for the models instances"""
        self.user = User.objects.create(
            username='Tester', email='tester@gmail.com', password='Test1234')
        self.profile = Profile(bio='This is my bio', photo='test.png', user=self.user)

    def tearDown(self):
        """Method to clear the model objects in the db after each testcase"""
        User.objects.all().delete()
        Profile.objects.all().delete()

    def test_instance(self):
        """Test case to check if created location is an instance of Location model class"""
        self.assertTrue(isinstance(self.profile, Profile))

    def test_save_profile(self):
        """Test case to check if created location is being saved in our database"""
        self.profile.save_profile()
        profiles = Profile.objects.all()
        self.assertTrue(len(profiles) > 0)

    def test_update_profile(self):
        """Test case to check if a saved location is being updated successfully"""
        self.profile.save_profile()
        self.profile.bio = 'I have edited'
        Profile.update_profile(self.profile)
        updated_profile = Profile.objects.get(id=self.profile.id)
        self.assertEqual(updated_profile.bio, 'I have edited')

    def test_delete_profile(self):
        """Test case to check if a saved location is being removed from our db when deleted."""
        self.profile.save_profile()
        self.profile.delete_profile()
        profiles = Profile.objects.all()
        self.assertTrue(len(profiles) == 0)


class ProjectTestCase(TestCase):
    """Test case for Picture model"""

    def setUp(self):
        """Set up for the models instances"""
        self.category = Category(name='Python')
        self.category.save()
        self.user = User.objects.create(
            username='Tester', email='tester@gmail.com', password='Test1234')
        self.project = Project(name='Portfolio', link='www.heroku.com', image='test.png',
                               description='Image description', pub_date='2022-02-02 12:22:10',
                               category=self.category, author=self.user)

    def tearDown(self):
        """Method to clear the model objects in the db after each testcase"""
        Category.objects.all().delete()
        User.objects.all().delete()
        Project.objects.all().delete()

    def test_instance(self):
        """Test case to check if created picture is instance of Picture model class"""
        self.assertTrue(isinstance(self.project, Project))

    def test_save_project(self):
        """Test case to check if created picture is being saved in our database"""
        self.project.save_project()
        projects = Project.objects.all()
        self.assertTrue(len(projects) > 0)

    def test_delete_project(self):
        """Test case to check if a saved picture is being removed from our db when deleted."""
        self.project.save_project()
        self.project.delete_project()
        projects = Project.objects.all()
        self.assertTrue(len(projects) == 0)

    def test_search_project_by_category(self):
        """Test case to check if we can search an image by category."""
        self.project.save_project()
        projects = Project.search_project_by_category('Food')
        self.assertTrue(len(projects) == 1)

    def test_filter_by_category(self):
        """Test case to check if we can filter an image by their location."""
        self.project.save_project()
        projects = Project.filter_by_category('Munich')
        self.assertEqual(len(projects), 1)
