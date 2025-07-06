from django.db import models

class Hospital(models.Model):
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=50)      # 시/도
    district = models.CharField(max_length=50)  # 시/군/구
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=20)

    def __str__(self):
        return self.name