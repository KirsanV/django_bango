from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    email = models.EmailField('Электронная почта', unique=True)

    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)
    phone_number = models.CharField('Телефон', max_length=20, blank=True)
    country = models.CharField('Страна', max_length=100, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email