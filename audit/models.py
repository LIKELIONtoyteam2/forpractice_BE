from django.db import models

# Create your models here.
GENDER_CHOICES = (
  (1, "woman"),
  (2, "man"),
)

class Hashtag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name
class Post(models.Model):
  title = models.CharField(max_length=200)
  date = models.DateTimeField(auto_now_add=True)
  body = models.TextField()
  gender = models.IntegerField(choices=GENDER_CHOICES, default=1)
  expiration_date = models.DateField()
  open_date = models.DateField()
  hashtag = models.ManyToManyField(Hashtag, related_name='posts', blank=True)

  def __str__(self):
    return self.title

  