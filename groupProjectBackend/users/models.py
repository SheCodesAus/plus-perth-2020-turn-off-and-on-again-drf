from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings
from PIL import Image

class CustomUser(AbstractUser):
    pass
    
    def __str__(self):
        return self.username

