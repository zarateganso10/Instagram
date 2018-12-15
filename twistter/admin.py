from django.contrib import admin
from django.contrib.admin import site

from twistter.models import PostText, Profile

# Register your models here.

admin.site.register(PostText)
admin.site.register(Profile)