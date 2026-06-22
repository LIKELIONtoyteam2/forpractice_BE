from django.db import models
from django.conf import settings

# Create your models here.
GENDER_CHOICES = (
  (1, "woman"),
  (2, "man"),
)

class Hashtag(models.Model):
    name = models.CharField(max_length=50, unique=True) #중복 해시태그 방지

    def __str__(self):
        return self.name
class Post(models.Model):
  author = models.ForeignKey(             # ✅ 추가
    settings.AUTH_USER_MODEL,
    on_delete=models.CASCADE,
    related_name='posts',
    null=True                             # 기존 데이터 때문에 null 허용
  )
  title = models.CharField(max_length=200)
  date = models.DateTimeField(auto_now_add=True)
  body = models.TextField()
  gender = models.IntegerField(choices=GENDER_CHOICES, default=1)
  expiration_date = models.DateField()
  open_date = models.DateField()
  hashtag = models.ManyToManyField(Hashtag, blank=True)
  photo = models.ImageField(blank=True, null=True, upload_to="post_photo")

  def __str__(self):
    return self.title

