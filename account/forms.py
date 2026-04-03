from dataclasses import field
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser
from django import forms

class RegisterForm(UserCreationForm):
  class Meta:
    model=CustomUser
    fields=['username','password1','password2','nickname','age','sex']
    widgets = {
            'sex_choice': forms.Select(attrs={'class': 'form-select'}),
        }
