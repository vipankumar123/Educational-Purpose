# models.py
from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    author = models.CharField(max_length=100)
    published_date = models.DateField()
