from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse

class Type(models.Model):
    name = models.CharField(max_length=32)

    def __str__(self):
        return self.name

class Location(models.Model):
    name = models.CharField(max_length=32)

    def __str__(self):
        return self.name

class Level(models.Model):
    name = models.CharField(max_length=32)

    def __str__(self):
        return self.name

class Audience(models.Model):
    name = models.CharField(max_length=32)

    def __str__(self):
        return self.name

class Listing(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    date_created = models.DateTimeField()
    start_date = models.DateTimeField()
    apply_by_date = models.DateTimeField()
    image = models.URLField()
    date_created = models.DateTimeField()
    typeList = models.ForeignKey(Type, null=True, blank=True, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, null=True, blank=True, on_delete=models.CASCADE)
    level = models.ForeignKey(Level, null=True, blank=True, on_delete=models.CASCADE)
    audience = models.ForeignKey(Audience, null=True, blank=True, on_delete=models.CASCADE)
    user = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name='user_listing'
    )

    def __str__(self):
        return self.title