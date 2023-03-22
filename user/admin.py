from django.contrib import admin
from .models import CustomUser, GitHubCredentials
# Register your models here.

admin.site.register(CustomUser)
admin.site.register(GitHubCredentials)
