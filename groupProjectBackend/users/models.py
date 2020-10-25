from django.contrib.auth.models import AbstractUser

from django.db import models
from django.conf import settings
from PIL import Image

class CustomUser(AbstractUser):
    pass
    
    def __str__(self):
        return self.username

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,blank=True, null=True, on_delete=models.CASCADE)
    logo = models.ImageField(default='default.jpg', upload_to='profile_pics', blank=True, null=True)
    organisation = models.TextField(max_length=150, blank=True)
    description = models.TextField(max_length=300, blank=True)
    website = models.URLField()

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self):
        super().save()
        # run the save method from the parents
        img = Image.open(self.avatar.path)
        if img.height > 300 or img.width > 300:
            output_size = (300,  300)
            img.thumbnail(output_size)
            img.save(self.avatar.path)