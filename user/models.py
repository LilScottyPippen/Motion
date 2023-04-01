from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .managers import CustomUserManager
from django.core.exceptions import ValidationError

class CustomUser(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=30)
    email = models.EmailField(unique=True, null=True)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_google = models.BooleanField(default=False)
    is_github = models.BooleanField(default=False)

    USERNAME_FIELD = "email"

    objects = CustomUserManager()
    def __str__(self):
        return f'Email: {self.email} | Username: {self.username}'

    def set_github_login(self, login):
        if login:
            self.is_github = True
            self.save()

    def set_google_login(self, login):
        if login:
            self.is_google = True
            self.save()


class GoogleCredentials(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    access_token = models.CharField(max_length=255)
    id_token = models.CharField(max_length=255)
    email = models.EmailField(blank=True)

    def __str__(self):
        return f'Email: {self.email}'

class GitHubCredentials(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    _id = models.CharField(max_length=255)
    login = models.CharField(max_length=255)

    def __str__(self):
        return f"Login: {self.login}"