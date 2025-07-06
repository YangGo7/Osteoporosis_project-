from django.db import models
from django.urls import reverse
app_name = 'osteoporosis'

class Osteoporosis(models.Model):
    name = models.CharField("이름", max_length=50)
    age = models.IntegerField("나이", default=0)
    gender = models.CharField("성별", max_length=10)
    height = models.IntegerField("키(cm)", default=0)
    weight = models.IntegerField("몸무게(kg)", default=0)

    # 위험 요소 (골절 관련 이력/질병 등)--(Boolean → 라디오버튼)
    fracture = models.BooleanField("골절 병력 여부", default=False)
    smoking = models.BooleanField("흡연 여부", default=False)
    drinking = models.BooleanField("음주 여부", default=False)
    calcitriol = models.BooleanField("비타민D 복용 여부", default=False)
    op = models.BooleanField("골다공증 진단 여부", default=False)
    ckd = models.BooleanField("만성 신장질환 여부", default=False)
    copd = models.BooleanField("만성 폐질환 여부", default=False)
    dm = models.BooleanField("당뇨병 여부", default=False)

    def __str__(self):
        return self.name



from django.db import models
from django.contrib.auth.models import User

class OsteoporosisResult(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    major_risk = models.FloatField()
    hip_risk = models.FloatField()
    level = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.level} ({self.created_at.strftime('%Y-%m-%d')})"

    class Meta:
        unique_together = ('user', 'name', 'major_risk', 'hip_risk', 'level')
# models.py
class OsteoporosisResult(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField(null=True)  # 추가
    gender = models.IntegerField(null=True)       # 추가
    height = models.FloatField(null=True)
    height = models.FloatField(null=True)
    major_risk = models.FloatField()
    hip_risk = models.FloatField()
    level = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
