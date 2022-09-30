from enum import unique
from unittest.util import _MAX_LENGTH
from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class InstaUser(AbstractUser):
    
    email = models.EmailField(max_length=128, unique=True)
    password = models.CharField(max_length=30)
    name = models.CharField(max_length=30)
    nickname = models.CharField(max_length=20)
    is_dating = models.BooleanField(null=True)
    username = None
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

