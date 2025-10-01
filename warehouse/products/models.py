from django.conf import settings
from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class Product(models.Model):
    name = models.CharField(max_length=100)
    type = models.ForeignKey('TypeProduct', on_delete=models.CASCADE, related_name='products', null=False)

    def __str__(self):
        return f'{self.name.capitalize()} type: {self.type}'

    class Meta:
        ordering = ['name']


class TypeProduct(models.Model):
    type = models.CharField(max_length=100, null=False, blank=False)
    date_to = models.DateField(null=False, blank=False, default=timezone.now)
    user_moderator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=False, related_name='user_moderator')
    # user_moderator = models.ForeignKey('auth.User', on_delete=models.CASCADE, null=False, related_name='user_moderator')

    def __str__(self):
        return f'Type: {self.type}'


class Storage(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    # type = models.ForeignKey('StorageType', on_delete=models.CASCADE, related_name='storages_type')
    product = models.ForeignKey('Product', on_delete=models.CASCADE, related_name='storages')

