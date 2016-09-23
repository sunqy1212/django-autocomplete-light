from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    ID_No = models.CharField(max_length=8)
    full_name = models.CharField(max_length=10)
    phone_number = models.CharField(max_length=11)
    def __str__(self):
        return self.full_name
    class Meta:
        verbose_name = 'UserProfile'
        verbose_name_plural = 'UserProfile'


# 操作票数据表
class CaoZuoPiao(models.Model):
    nipiaoren = models.CharField(max_length=10)

    def __str__(self):
        return self.nipiaoren