from unicodedata import category
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=255, blank=False)

    def __str__(self):
        return self.name

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=255, blank=False)
    price = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.title
