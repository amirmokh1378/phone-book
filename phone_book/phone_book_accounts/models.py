from django.db import models
import datetime


# Create your models here.


class AnonymousAccount(models.Model):
    username = models.CharField(max_length=100, unique=True)
    created_time = models.DateTimeField(default=datetime.datetime.now())
    expire_time = models.DateTimeField(default=(datetime.datetime.now() + datetime.timedelta(days=2)))
