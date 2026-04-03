from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUser(AbstractUser):
  sex_choice=[
    ('여자', '여자'),
    ('남자', '남자'),
  ]
  nickname=models.CharField(max_length=100)
  age=models.CharField(max_length=50)
  sex=models.CharField(max_length=10, default='여자', choices=sex_choice, verbose_name="성별")
  
  