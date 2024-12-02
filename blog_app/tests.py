from django.test import TestCase
from django.test import Client
from django.contrib.auth import get_user_model
from .models import Create_Blog

# Create your tests here.

class BlogViewTest(TestCase):
    def setUp(self):
        # Create a user and a blog post for the tests
        self.user = get_user_model().objects.create_user(username='testuser', password='password123')
        self.blog = Create_Blog.objects.create(
            user=self.user,
            blog_title="Test Test",
            blog_entry="This is a test blog post"
        )
        self.client = Client()

class UserViewsTest(TestCase):
    def setUp(self):
        # Create a user for the tests
        self.user = get_user_model().objects.create_user(username='testuser', password='password123')
