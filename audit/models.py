from django.db import models

# Create your models here.
class Post(models.Model):
  name = models.CharField(max_length=50)
  expiration = models.TextField(max_length=500)
  open = models.TextField(max_length=500)
  created_at = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return self.name
