from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager
from django.utils.timezone import now


class CustomUserManager(UserManager):
    pass


class CustomUser(AbstractUser):
    id = models.CharField(max_length=30)
    sid = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='SID')
    nick = models.CharField(max_length=30)
    stud_no = models.IntegerField(default=207777777, null=False)
    email = models.CharField(null=False, max_length=128)
    pw_hash = models.CharField(null=False, max_length=128)
    pnt = models.IntegerField(default=0)
    registered = models.DateTimeField(default=now, null=False)
    pw_reset_time = models.DateTimeField(default=now, null=False)
    unregistered = models.DateTimeField(null=True)
    objects = CustomUserManager()


class NavigationGroup(models.Model):
    name = models.CharField(max_length=30, null=False)
    priority = models.FloatField(default=0.0, null=False)


class NavigationItem(models.Model):
    name = models.CharField(max_length=30, null=False)
    group = models.OneToOneField(
        NavigationGroup,
        on_delete=models.CASCADE,
    )
    created = models.DateTimeField(default=now, null=False)
    hidden = models.BooleanField(default=False, null=False)
    priority = models.FloatField(default=0.0, null=False)


class Board(NavigationItem):
    counter = models.IntegerField()


class Article(models.Model):
    title = models.CharField(max_length=128)
    content = models.CharField(max_length=10000)
    board = models.OneToOneField(
        Board,
        on_delete=models.CASCADE,
    )
    author = models.OneToOneField(
        CustomUser,
        on_delete=models.CASCADE,
    )
    created = models.DateTimeField(default=now, null=False)
    modified = models.DateTimeField(default=now, null=False)
    upvote = models.IntegerField(default=0, null=False)
    downvote = models.IntegerField(default=0, null=False)
    hidden = models.BooleanField(default=False, null=False)
