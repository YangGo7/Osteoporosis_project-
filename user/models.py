from django.contrib.auth.models import User
from django.db import models

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.IntegerField(null=True, blank=True)  # 나이
    gender = models.CharField(max_length=10, null=True, blank=True)  # 성별 (Male/Female)
    height = models.FloatField(null=True, blank=True)  # 키
    weight = models.FloatField(null=True, blank=True)  # 몸무게
    fracture = models.BooleanField(default=False)  # 골절 여부
    smoking = models.BooleanField(default=False)  # 흡연 여부
    calcitriol = models.BooleanField(default=False)  # 칼시트리올 복용 여부
    op = models.BooleanField(default=False)  # 골다공증 여부
    ckd = models.BooleanField(default=False)  # 만성 신장병 (Chronic Kidney Disease)
    copd = models.BooleanField(default=False)  # 만성 폐쇄성 폐질환 (Chronic Obstructive Pulmonary Disease)
    dm = models.BooleanField(default=False)  # 당뇨병 (Diabetes Mellitus)
    drinking = models.BooleanField(default=False)  # 음주 여부

    def __str__(self):
        return f"{self.user.username}'s Profile"
