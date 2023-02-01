from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator


class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    image = models.ImageField(upload_to='media/')

    def __str__(self):
        return self.name

