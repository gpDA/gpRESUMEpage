from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    age = models.CharField(max_length=2, default='10')
    image = models.CharField(max_length=256, default='https://api.adorable.io/avatars/285/abott@adorable')
    def __str__(self):
        return self.email