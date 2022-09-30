from enum import unique
from unittest.util import _MAX_LENGTH
from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

# 220930 최해민 커스텀 유저모델을 만들고, 장고가 제공해주는 기본 유저 인증 과정을 사용함
class InstaUser(AbstractUser):
    
    email = models.EmailField(max_length=128, unique=True)
    password = models.CharField(max_length=30)
    name = models.CharField(max_length=30)
    nickname = models.CharField(max_length=20)
    is_dating = models.BooleanField(null=True)
    username = None
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

