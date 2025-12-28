from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from auth.manager import CustomUserManager
# Create your models here.

class AuthUser(AbstractBaseUser, PermissionsMixin):
    GenderChoice = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Prefer not to say', 'Prefer not to say'),

    )
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    gender = models.CharField(max_length=100, choices=GenderChoice, default='Prefer not to say')
    country = models.CharField(max_length=100, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    profile_image = models.CharField(max_length=100, blank=True, null=True, default='default_profile.png')
    date_joined = models.DateTimeField(auto_now_add=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)


    objects = CustomUserManager()

    def __str__(self):
        return self.username