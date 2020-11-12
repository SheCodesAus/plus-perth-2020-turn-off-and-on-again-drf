import os
import uuid
from django.db import models
from django.contrib.auth import get_user_model
from django.utils.text import slugify
from django.urls import reverse
# from PIL import Image
from django.utils.timezone import now
from datetime import datetime   


def upload_image_to(self, filename):
        print(filename)
        filename_base, filename_ext = os.path.splitext(filename)
        print(os.path.splitext(filename))
        u = uuid.uuid4()
        return 'posts/%s/%s' % (
            now().strftime("%Y%m%d"),
            u.hex
        )

class Type(models.Model):
    name = models.CharField(max_length=32)
    slug = models.SlugField(unique=True)
    image = models.ImageField(default=None, upload_to=upload_image_to, blank=True, null=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Type,self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('type-detail', kwargs={'slug': self.slug})

class Location(models.Model):
    name = models.CharField(max_length=32)
    slug = models.SlugField(unique=True)
    image = models.ImageField(default=None, upload_to=upload_image_to, blank=True, null=True)


    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Location,self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('location-detail', kwargs={'slug': self.slug})

class Level(models.Model):
    name = models.CharField(max_length=32)
    slug = models.SlugField(unique=True)
    image = models.ImageField(default=None, upload_to=upload_image_to, blank=True, null=True)


    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Level,self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('level-detail', kwargs={'slug': self.slug})
        

class Audience(models.Model):
    name = models.CharField(max_length=32)
    slug = models.SlugField(unique=True)
    image = models.ImageField(default=None, upload_to=upload_image_to, blank=True, null=True)


    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Audience,self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('audience-detail', kwargs={'slug': self.slug})

class Listing(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    date_created = models.DateTimeField(default=datetime.now, blank=True)
    start_date = models.DateTimeField()
    apply_by_date = models.DateTimeField()
    image = models.ImageField(default=None, upload_to=upload_image_to, blank=True, null=True)
    # image = models.URLField()
    link = models.URLField()
    date_created = models.DateTimeField()
    eligibility = models.TextField()
    audience = models.ManyToManyField(Audience)
    typeList = models.ManyToManyField(Type)
    location = models.ManyToManyField(Location)
    level = models.ManyToManyField(Level)
    owner = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name='owner_listing'
    )
    organisation = models.ForeignKey(
    'organisations.Organisation',
    on_delete=models.CASCADE,
    null=True,
    blank=True
    )

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        super(Listing, self).save(*args, **kwargs)

        # img = Image.open(self.image.path)
        # if img.height > 300 or img.width > 300:
        #     output_size = (300,  300)
        #     img.thumbnail(output_size)
        #     img.save(self.image.path)
