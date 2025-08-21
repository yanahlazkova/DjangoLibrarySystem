import uuid

from django.db import models


class User(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    age = models.IntegerField()
    email = models.EmailField(null=False, unique=True)
    login = models.CharField(max_length=255, null=True)
    password = models.CharField(max_length=255, null=True)
    phone = models.CharField(max_length=30, null=True, unique=True)
