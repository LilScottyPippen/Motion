from django.contrib import admin
from .models import CustomUser, GoogleCredentials
# Register your models here.

admin.site.register(CustomUser)
admin.site.register(GoogleCredentials)
