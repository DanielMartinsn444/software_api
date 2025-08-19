from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class Usuario(models.Model):
    username = models.CharField(max_length=30, unique=True)
    password = models.CharField(max_length=128)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.username
