from django.urls import path
from .views import *
from . import views

app_name='audit'
urlpatterns=[
  path('', home, name='home'),
  path('post/<int:post_id>', detail, name='detail'),
  path('new/', new, name="new"),
  path('create/', create, name="create"),
  path('delete/<int:post_id>', delete, name="delete"),
  path('update_page/<int:post_id>', update_page, name="update_page"),
  path('update_post/<int:post_id>', update_post, name="update_post"),
]