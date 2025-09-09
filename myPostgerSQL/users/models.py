import uuid

from django.db import models


class User(models.Model):
    firstname = models.CharField(max_length=255, null=True)
    lastname = models.CharField(max_length=255, null=True)
    age = models.IntegerField(null=True)
    phone = models.CharField(max_length=30, null=True, unique=True)

    def __str__(self):
        return f'{self.firstname} {self.lastname} {self.age} {self.phone}'

class Account(models.Model):
    email = models.EmailField(null=False, unique=True)
    login = models.CharField(max_length=255, null=False)
    password = models.CharField(max_length=255, null=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f'{self.email} {self.login} {self.password} {self.user}'

