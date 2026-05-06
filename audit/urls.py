from django.urls import path
from .views import *

app_name = 'audit'

urlpatterns =[
  path('', PostListView.as_view()),
  path('<int:pk>/', PostDetailView.as_view()),
]