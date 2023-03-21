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
    github_id = models.CharField(max_length=255, unique=True, null=True)
    username = models.CharField(max_length=30, validators=[existUsername])
    email = models.EmailField(unique=True, null=True, validators=[existEmail])
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = "email"

    objects = CustomUserManager()
    def __str__(self):
        return self.username
