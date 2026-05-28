from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
  email = models.EmailField(max_length=100, unique=True)
  nickname = models.CharField(max_length=100, default='')
  profile_image = models.ImageField(upload_to='profile/', null=True, blank=True)
  header_image = models.ImageField(upload_to='header/', null=True, blank=True)