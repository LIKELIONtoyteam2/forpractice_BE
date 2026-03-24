from django.db import models
from django.utils import timezone

# Create your models here.
class Post(models.Model):
  name = models.CharField(max_length=50)
  expiration = models.TextField(max_length=500)
  open = models.TextField(max_length=500)
  created_at = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return self.name
# audit/models.py (기존 코드 아래에 추가하세요)

from django.utils import timezone # 상단에 이 줄이 없다면 추가해 주세요.

class Inventory(models.Model):
    name = models.CharField(max_length=50) # 상품명
    category = models.CharField(max_length=20, default='기타') # 카테고리 (간단하게 텍스트로 시작)
    expiration_date = models.DateField() # 유통기한 (날짜형)
    opened_date = models.DateField(null=True, blank=True) # 개봉일자 (안 뜯었을 수도 있으니 비워둘 수 있게 설정)
    
    # 디데이를 계산해주는 똑똑한 함수
    def get_d_day(self):
        today = timezone.now().date()
        d_day = (self.expiration_date - today).days
        return d_day

    def __str__(self):
        return self.name