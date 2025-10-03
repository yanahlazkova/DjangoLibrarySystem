from django.conf import settings
from django.db import models

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(
        max_length=150,
        db_index=True) # db_index - для швидкішого пошуку
    content = models.TextField()
    image_url = models.URLField(
        max_length=500, blank=True, null=True
    )
    slug = models.SlugField(max_length=150, unique=True) # для більш зрозумілого url (тільки літери, цифри, _, -, #)
    body = models.TextField(blank=True, db_index=True) # blank=True - може бути пустим
    date_pub = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
