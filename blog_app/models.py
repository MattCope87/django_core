from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

class Create_Blog(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    blog_title = models.CharField(max_length=85)
    blog_entry = models.CharField(max_length=300)
    blog_image = models.ImageField(upload_to="blogs", blank=True, null=True)
    blog_view_count = models.PositiveBigIntegerField(default=1)
    blog_date = models.DateTimeField(default=timezone.now)

class Comment(models.Model):
    blog = models.ForeignKey(Create_Blog, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)