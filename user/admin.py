from django.contrib import admin
from .models import CustomUser, GoogleCredentials, GitHubCredentials
# Register your models here.

admin.site.register(CustomUser)
admin.site.register(GoogleCredentials)
admin.site.register(GitHubCredentials)
