from django import forms
from .models import Post

class PostForm(forms.ModelForm):
  class Meta:
    model=Post
    fields=['name', 'expiration', 'open']
    widgets = {
      'expiration': forms.DateInput(attrs={'type':'date'}),
      'open': forms.DateInput(attrs={'type':'date'}),
    }