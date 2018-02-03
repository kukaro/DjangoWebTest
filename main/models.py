from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager
import time


class CustomUserManager(UserManager):
    pass


class CustomUser(AbstractUser):
    id = models.CharField(max_length=30)
    sid = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='SID')
    nick = models.CharField(max_length=30)
    stud_no = models.IntegerField(null=False)
    email = models.CharField(null=False, max_length=128)
    pw_hash = models.CharField(null=False, max_length=128)
    pnt = models.IntegerField(default=0)
    registered = models.DateTimeField(default=time.localtime(), null=False)
    pw_reset_time = models.DateTimeField(default=time.localtime(), null=False)
    unregistered = models.DateTimeField(null=True)
    objects = CustomUserManager()
