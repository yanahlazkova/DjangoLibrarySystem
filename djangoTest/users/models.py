import uuid

from django.db import models


class User(models.Model):
    login = models.CharField(max_length=255, null=True)
    password = models.CharField(max_length=255, null=True)
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    phone = models.CharField(max_length=20, null=True, unique=True)
    email = models.EmailField(null=False, unique=True)


