from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import Create_Blog, Comment

admin.site.register(Create_Blog)
admin.site.register(Comment)