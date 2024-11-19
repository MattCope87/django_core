from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

class Create_Event(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    ev_name = models.CharField(max_length=85)
    ev_desc = models.CharField(max_length=300)
    ev_image = models.ImageField(upload_to="EventManager", blank=True, null=True)
    ev_view_count = models.PositiveBigIntegerField(default=1)
    ev_date = models.DateTimeField(default=timezone.now)
    ev_location = models.CharField(max_length=50, null=True)
    attendees = models.ManyToManyField(User, related_name='rsvps', blank=True)
