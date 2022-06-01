from django.db import models
from django.utils import timezone

class Article(models.Model):
    title = models.CharField(max_length=300)
    slug = models.SlugField(primary_key=True, unique=True)
    content = models.TextField()
    publishAt = models.DateTimeField(default=timezone.now)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
