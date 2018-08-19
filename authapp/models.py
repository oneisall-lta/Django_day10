from django.contrib.auth.models import AbstractUser
from django.db import models


class MyUserModel(AbstractUser):
    tel = models.CharField(max_length=12)
    qq = models.CharField(max_length=20, null=True)

