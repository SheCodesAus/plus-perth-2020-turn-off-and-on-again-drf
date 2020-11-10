from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings
from PIL import Image


class CustomUser(AbstractUser):
    is_invited = models.BooleanField(default=False)
    organisation = models.ForeignKey(
        'organisations.Organisation',
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )
    
    def __str__(self):
        return self.username

