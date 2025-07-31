import uuid

from django.db import models


class Book(models.Model):
    id = models.IntegerField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    book_id = models.CharField(max_length=255, default=uuid.uuid4, unique=True)
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    year = models.IntegerField()
    ebook = models.BooleanField()
    filename = models.CharField(max_length=255, null=True)
    genre = models.CharField(max_length=255, null=True)


class Reader(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)

