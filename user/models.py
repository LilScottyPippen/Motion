from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .managers import CustomUserManager
from django.core.exceptions import ValidationError

def existEmail(email):
    if CustomUser.objects.filter(email=email).exists():
        raise ValidationError('This email address already exists.')
    return email

def existUsername(username):
    if CustomUser.objects.filter(username=username).exists():
        raise ValidationError('This username already exists.')
    return username
class CustomUser(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=30, validators=[existUsername])
    email = models.EmailField(unique=True, null=True, validators=[existEmail])
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = "email"

    objects = CustomUserManager()
    def __str__(self):
        return f'Email: {self.email} | Username: {self.username}'

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