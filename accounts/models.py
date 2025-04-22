# accounts/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    # boshqa maydonlar

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='customuser_set',  # Yangi related_name
        blank=True,
        help_text='The groups this user belongs to.'
    )

    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='customuser_permissions',  # Yangi related_name
        blank=True,
        help_text='Specific permissions for this user.'
    )
