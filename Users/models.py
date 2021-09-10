from django.db import models

from django.contrib.auth.models import AbstractUser
# Create your models here.

class BlogUser(AbstractUser):
    age = models.IntegerField()
    email = models.EmailField(unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []