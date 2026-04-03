from django.db import models
from datetime import date
from django.utils import timezone

# Create your models here.

class Hashtag(models.Model):
   hashtag=models.CharField(max_length=100)

   def __str__(self):
      return self.hashtag
   
class Post(models.Model):
  name = models.CharField(max_length=50)
  expiration = models.DateField() #유통기한
  open = models.DateField()
  created_at = models.DateTimeField(auto_now_add=True)
  photo = models.ImageField(blank=True, null=True, upload_to="post_photo")
  hashtag = models.ManyToManyField(Hashtag)

  def get_d_day(self):
     today = date.today()
     delta = self.expiration - today
     return delta.days
  
  def from_open(self):
     today = date.today()
     delta = today - self.open
     return delta.days

  def __str__(self):
    return self.name
