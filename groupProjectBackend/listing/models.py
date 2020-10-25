from django.db import models
from django.contrib.auth import get_user_model
from django.utils.text import slugify
from django.urls import reverse

class Type(models.Model):
    name = models.CharField(max_length=32)
    slug = models.SlugField(unique=True)

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
    date_created = models.DateTimeField()
    start_date = models.DateTimeField()
    apply_by_date = models.DateTimeField()
    image = models.URLField()
    link = models.URLField()
    date_created = models.DateTimeField()
    typeList = models.ForeignKey(Type, null=True, blank=True, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, null=True, blank=True, on_delete=models.CASCADE)
    level = models.ForeignKey(Level, null=True, blank=True, on_delete=models.CASCADE)
    audience = models.ForeignKey(Audience, null=True, blank=True, on_delete=models.CASCADE)
    owner = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name='owner_listing'
    )

    def __str__(self):
        return self.title